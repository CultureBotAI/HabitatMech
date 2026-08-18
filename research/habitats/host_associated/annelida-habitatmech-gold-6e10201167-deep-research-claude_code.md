---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:07:15.943440'
end_time: '2026-08-17T20:15:02.598603'
duration_seconds: 466.66
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Annelida
  habitat_identifier: habitatmech:GOLD.6e10201167
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Annelida'
  assertions: '150'
  parent_terms: ENVO:01001000
  xrefs: NCBITaxon:6340
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term NCBITaxon:6340 'Annelida' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.6e10201167)"
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
  web_search_requests: 17
  num_turns: 39
  total_cost_usd: 3.6676760000000006
  session_id: 8fc8c1d3-4ac5-4123-965f-d9307275d778
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 38
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Annelida
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.6e10201167
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Annelida
- **Upstream assertion volume:** 150
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** NCBITaxon:6340

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term NCBITaxon:6340 'Annelida' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.6e10201167)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Annelida** as a microbial habitat, with citations.

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

# Annelida (habitatmech:GOLD.6e10201167) — definition research

> **Proposed definition:** An animal-associated environment which is determined by an annelid — a segmented, coelomate worm of the phylum Annelida (NCBITaxon:6340), whether marine polychaete, clitellate earthworm or leech, or siboglinid tubeworm.

ENVO-idiomatic short form, matching the wording already used at `plant-associated environment`, `animal-associated environment`, `fungi-associated environment` and `cnidarian-associated environment`: **"An environmental system determined by an annelid."** The longer form above is preferable for HabitatMech because the differentia (which worms count) is the part a curator will be asked about, and "worm" is the single most overloaded common name in host-associated metadata.

**Recommended disposition:** keep the minted identifier; file a term request for `annelid-associated environment` under `ENVO:01001002` (not `ENVO:01001000`, which is what the record currently carries — see §2.4); keep `NCBITaxon:6340` as `relation: xref`.

---

## 1. What the concept denotes

### 1.1 The reading the data means

The GOLD subtree settles this. `Host-associated > Annelida` is not a leaf: it is the root of a 23-path host subtree in `data/raw/gold_ecosystem_paths.tsv`, whose children are **anatomical compartments of an annelid body**, plus one excreted product:

| GOLD path below `Host-associated > Annelida` | assertions |
|---|---|
| `> Digestive system` | 11 |
| `> Tissue` | 4 |
| `> Digestive system > Digestive tube > Cast` | 3 |
| `> Intracellular endosymbionts > Trophosome` | 3 |
| `> Digestive system > Crop` | 2 |
| `> Excretory system > Nephridia` | 2 |
| `> Integument`, `> Whole body` | 1 each |
| `> Coelom`, `> Coelom > Trophosome`, `> Gills`, `> Integument > Cuticle`, `> Integument > Cuticle > Epibionts`, `> Integument > Subcuticular space`, `> Reproductive system > Egg capsule`, `> Reproductive system > Egg capsule > Extracellular`, `> Digestive system > Digestive tube > Extracellular symbionts` | 0 |

The node itself carries 150 assertions with `assertion_unit: ORGANISM` — i.e. 150 sequenced organisms whose recorded habitat is "an annelid, compartment unspecified or not resolved by the curator." That is the concept: **the living body of an annelid worm, taken as a whole, as the environment a microorganism inhabits and a sample is drawn from.**

The presence of both `Trophosome` (a siboglinid tubeworm organ; ENVO:01000165, "a specialised organ found in deep-sea tube worms populating hydrothermal vent environments that is colonised by chemosynthetic bacteria") and `Cast` and `Nephridia` (earthworm-specific) under one parent confirms that GOLD's Annelida spans the modern, post-2011 circumscription of the phylum — marine tubeworms *and* terrestrial earthworms — not the older "Polychaeta + Oligochaeta + Hirudinea" textbook triad.

### 1.2 What is inside the concept

- The whole living annelid body as a microbial habitat, at the resolution "annelid," when no finer compartment is recorded.
- By subsumption (as parent of the child records, not as content of this record): gut lumen and gut wall, crop, coelomic fluid, nephridia, trophosome, cuticle and subcuticular space, gills, egg capsule/cocoon, epidermal epibiont layer.
- Both symbiotic and transient/passenger microbiota — GOLD does not distinguish, and neither should the definition. Earthworm gut microbiota are substantially ingested soil organisms that are transiently stimulated ([Drake & Horn 2007](https://doi.org/10.1146/annurev.micro.61.080706.093139)); siboglinid trophosome microbiota are an obligate monoculture ([Bright & Giere 2005](https://dalspace.library.dal.ca/bitstream/handle/10222/78095/VOLUME%2038-NUMBER%201-2005-PAGE%201.pdf)). Both are annelid-associated environments.

### 1.3 What is a neighbouring concept, not this one

- **Each anatomical part.** HabitatMech already holds these as separate records — `cast.yaml`, `trophosome.yaml`, `nephridium.yaml` (`BTO:0000923`), `coelom.yaml` (`BTO:0001707`). Per the repo's part/whole rule, those ground to anatomy terms; this record does not.
- **Earthworm casts, vermicompost, and the drilosphere.** GOLD files `Cast` *under* the digestive tube, which is a defensible upstream choice, but a cast is expelled material sitting in soil, and its community is measurably *not* the same as gut content: in *Pontoscolex corethrurus* mesocosms, anterior and posterior gut sections were dominated by different taxa than casts, so casts are not simply deposited gut contents ([Microniches at the soil–plant–earthworm interface, *Eur J Soil Biol* 2023](https://www.sciencedirect.com/science/article/abs/pii/S1164556323000675)); compartment identity (bulk soil / drilosphere / gut wall / gut content / cast) is the primary structuring factor for bacterial community composition ([Zhang et al., *Pedosphere* 2023](https://www.sciencedirect.com/science/article/abs/pii/S1002016023001108)). Vermicompost and worm castings already have terms outside ENVO (`AGRO:00002042` vermicompost, `AGRO:00002043` worm castings). **Recommendation:** the cast record should not be dragged into the scope of this definition; if anything, flag `cast.yaml` (currently parented to `UBERON:0001555` digestive tract) for a separate look.
- **Burrows, tubes and burrow linings.** These are worm-modified sediment/soil, not the worm. ENVO's only annelid-flavoured term of this kind is `ENVO:01001111` *fossil worm burrow* — a geological feature, and an explicitly fossilised one.
- **The hydrothermal vent or whale-fall itself.** The chimney wall *Alvinella pompejana* colonises, and the whale bone *Osedax* bores into, are ENVO marine environments; the worm living in them is this concept.
- **The taxon `NCBITaxon:6340`.** A phylum is a class of organisms, not a place. It belongs as `relation: xref`, exactly as the curation note states.

### 1.4 Ambiguity in the label

"Annelida" itself is not ambiguous — it is a formal taxon name. Two real ambiguities sit behind it:

1. **Circumscription.** Whether Sipuncula, Echiura, Myzostomida and Siboglinidae (= former phyla Pogonophora/Vestimentifera) are inside Annelida. They are, on current phylogenomic evidence: Struck et al. recovered chaetopterids, myzostomids and sipunculids in the basal part of the annelid tree, with the remainder splitting into Errantia and Sedentaria (the latter containing Clitellata) ([*Nature* 471:95–98, 2011](https://doi.org/10.1038/nature09864); PMID [21368831](https://pubmed.ncbi.nlm.nih.gov/21368831/)). WoRMS lists Annelida (Lamarck, 1802) as accepted with Clitellata, Polychaeta and Sipuncula among its direct children ([WoRMS AphiaID 882](https://www.marinespecies.org/aphia.php?p=taxdetails&id=882)). The GOLD subtree's `Trophosome` child means GOLD is already using the inclusive reading. **The definition should follow the taxon and not enumerate exhaustively** — enumerations go stale as the phylum is revised.
2. **Common-name spill.** Sample metadata saying "worm" may mean a nematode, a flatworm, a priapulid, or an insect larva. This is a *synonym-hygiene* problem, not a definitional one (§5).

---

## 2. Genus — the broader kind

### 2.1 The match

**`ENVO:01001002` — animal-associated environment**, defined "An environmental system determined by an animal" ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)). Annelida is unambiguously within Animalia, so this is a true and minimal genus. It is also the parent used by every sibling term request already in `curation/term_requests.tsv` (human-, mammal-, sponge-, nematode-associated environment), so adopting it keeps the corpus internally consistent.

### 2.2 The precedent that this shape is acceptable to ENVO

`ENVO:01001179` **cnidarian-associated environment** — "An environmental system determined by a cnidarian or part of a cnidarian" — is a direct child of `ENVO:01001002` and is a phylum-level host-clade term. ENVO already does exactly what this term request asks for, one clade over. This is the single strongest argument for the request and should be cited in it.

### 2.3 Near-misses in ENVO, and why each fails

| CURIE | Label | Why it is not a match |
|---|---|---|
| `ENVO:01001176` | environment associated with an aquatic invertebrate | **Narrower and over-asserting.** Its definition requires "a habitat that is found in an aquatic environmental system." Earthworms are terrestrial; most leeches are freshwater-to-humid-terrestrial. Grounding here would assert aquatic habitat for the majority of the phylum's described species and would silently merge annelids with molluscs, cnidarians, sponges and aquatic arthropods. |
| `ENVO:01001055` | environment associated with an animal part or small animal | **Wrong axis.** It asserts either partitivity or small body size. Annelids range from interstitial gutless phallodrilines to 1.5 m *Riftia*; the concept is the whole organism at any size. |
| `ENVO:01001000` | environmental system determined by an organism | **Too broad** — this is the grandparent, covering plants, fungi and microbes. It is what the record currently carries as `parent_habitats`, which is a defect worth fixing independently of the term request (§6.3). |
| `ENVO:01000165` | trophosome | **Narrower, and part-level.** Applies to one family (Siboglinidae) and one organ. Already correctly used on `trophosome.yaml`. |
| `ENVO:01001111` | fossil worm burrow | **Wrong kind.** A fossilised channel in soil: a geological feature produced by a dead annelid, not an environment determined by a living one. |
| `NCBITaxon:6340` | Annelida | **Not a place.** A taxon term denotes a class of organisms. Correct as `xref` (issue #99 pattern). |
| `AGRO:00002042` / `AGRO:00002043` | vermicompost / worm castings | **Downstream product, and outside the host.** Relevant to the `cast` record, not to this one. |
| — | UBERON | **No candidate.** UBERON is an anatomy ontology; it has no whole-organism class for a phylum. Its annelid-relevant content is anatomical (e.g. `UBERON:0011997` coelom) — parts, per the repo's part/whole rule. |
| — | BTO | **Parts only.** BTO holds annelid-specific *anatomy* — `BTO:0004198` prostomium, `BTO:0004063` chloragogen cell, `BTO:0002857` eleocyte, `BTO:0006533` branchial crown, `BTO:0000923` nephridium — confirming that the only ontology coverage of annelids as habitat is at the part level, never the whole. |

**Conclusion: no existing term names this concept.** UNGROUNDED is correct.

---

## 3. Differentia — what distinguishes it from its siblings

The differentia is the **host clade**, and there is more physical content behind it than in most host-clade terms, because annelid body plans create several structurally distinct microbial microhabitats that other invertebrate phyla do not offer in combination. A curator can defend any of the following as supporting material; the definition sentence itself should carry only the clade.

**a. Segmented coelomate body plan with metameric excretory organs.** Nephridia are a per-segment habitat with their own resident, host-specific, vertically transmitted symbiont: almost all lumbricid earthworms harbour species-specific extracellular *Verminephrobacter* (Betaproteobacteria) in their nephridia, transmitted via the cocoon and co-speciating with the host for ~100 My ([Lund et al., *FEMS Microbiol Ecol* 2010 / review in PMC3975124](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3975124/)); the nephridial community also includes *Ca.* Nephrothrix ([Møller et al., *FEMS Microbiol Ecol* 2018](https://academic.oup.com/femsec/article/94/2/fix178/4768062)). Symbiont presence advances sexual maturation and raises hatching success ([Lund et al., *Appl Environ Microbiol* 76:4738, 2010](https://doi.org/10.1128/AEM.00108-10)).

**b. A through-gut that functions as a mobile anoxic microzone.** Directly measured in situ: the earthworm gut is anoxic, pH 6.9, ~50% water, enriched in total C, organic C and total N relative to the surrounding soil, with a C/N of 7 ([Horn, Schramm & Drake, *Appl Environ Microbiol* 69:1662–1669, 2003](https://doi.org/10.1128/AEM.69.3.1662-1669.2003); PMID [12620857](https://pubmed.ncbi.nlm.nih.gov/12620857/)). The consequence is functional, not just compositional: gut passage selectively stimulates ingested soil denitrifiers and fermenters, producing in vivo emission of N₂ and N₂O by the worm ([Drake & Horn, *Annu Rev Microbiol* 61:169–189, 2007](https://doi.org/10.1146/annurev.micro.61.080706.093139)). These are measurable physicochemical properties — the strongest kind of differentia available here.

**c. A blood-diet gut of exceptional simplicity.** In the medicinal leech *Hirudo verbana*, two cultivable species — *Aeromonas veronii* and *Mucinivorans hirudinis* — account for >95% (in some samples ~97%) of the crop community, against 500–10,000 taxa in a mammalian gut ([Graf, Kikuchi & Rio, *Trends Microbiol* 2006](https://doi.org/10.1016/j.tim.2006.06.009); [Maltz & Graf, *Gut Microbes* 3:4, 2012](https://doi.org/10.4161/gmic.20227)). The structure is conserved in the New World leech *Macrobdella decora* ([*Appl Environ Microbiol* 2021](https://doi.org/10.1128/AEM.02082-20)). Leech bladders carry an entirely different consortium.

**d. Chemosynthetic endosymbiosis, evolved repeatedly and in several body compartments.** Annelida is the phylum where this is most diverse ([Bright & Giere, *Symbiosis* 38:1–45, 2005](https://dalspace.library.dal.ca/bitstream/handle/10222/78095/VOLUME%2038-NUMBER%201-2005-PAGE%201.pdf)):
- *Trophosome, intracellular* — *Riftia pachyptila* bacteriocytes house a single 16S phylotype, "*Ca.* Endoriftia persephone," at up to 10⁹ cells g⁻¹ fresh trophosome, 15–35% of host body volume (Stewart & Cavanaugh 2006, as relayed in [Hinzke et al., *eLife* 2021](https://elifesciences.org/articles/58371) and [Hinzke et al., *mBio* 2019](https://doi.org/10.1128/mBio.02243-19)).
- *Subcuticular space, extracellular* — gutless phallodriline oligochaetes (*Olavius*, *Inanidrilus*) have no mouth, gut, anus or nephridia and carry a multi-member consortium just beneath the cuticle: *Ca.* Thiosymbion plus sulfate-reducing deltaproteobacteria and a spirochaete, with syntrophic sulfur cycling ([Dubilier et al., *Nature* 411:298–302, 2001](https://doi.org/10.1038/35077067); [Woyke et al., *Nature* 443:950–955, 2006](https://doi.org/10.1038/nature05192); [Kleiner et al., *PNAS* 109:E1173, 2012](https://doi.org/10.1073/pnas.1121198109)). Metagenomes of 231 individuals from 63 host species across 17 sites show *Ca.* Thiosymbion as an early, persistent acquisition with secondary symbionts convergently gained many times over ~150 My ([bioRxiv 10.1101/2021.04.28.441735](https://doi.org/10.1101/2021.04.28.441735) — **preprint; treat as unpublished**).
- *Root tissue* — *Osedax* bone-eating siboglinids lack a trophosome and instead house Oceanospirillales (near *Neptunomonas*) in bacteriocytes of vascularised roots that penetrate whale bone ([Goffredi et al. 2005/2007; Verna et al., *Environ Microbiol* 2010](https://doi.org/10.1111/j.1462-2920.2010.02299.x)).
- *Genomic contrast* — heterotrophic *Osedax frankpressi* symbionts show genome compaction and gene loss, unlike chemoautotrophic vestimentiferan symbionts ([Martínez-Redondo et al., *Nat Commun* 14, 2023](https://doi.org/10.1038/s41467-023-38521-6)).

**e. Dorsal epibiotic mats on the living cuticle.** *Alvinella pompejana* carries a 12–15 phylotype epibiotic community, >98% Campylobacterota (formerly Epsilonproteobacteria), as hair-like filaments from dorsal intersegmental mucous glands — absent from gills and tentacles, and host-regulated by the antimicrobial peptide alvinellacin ([Haddad et al., *Appl Environ Microbiol* 61:1679–1687, 1995](https://doi.org/10.1128/aem.61.5.1679-1687.1995); [Cary et al., *Appl Environ Microbiol* 63:1124–1130, 1997](https://doi.org/10.1128/aem.63.3.1124-1130.1997); [Tasiemski et al., *PLOS ONE* 2014](https://doi.org/10.1371/journal.pone.0095737)). This is what GOLD's `Integument > Cuticle > Epibionts` path is for.

**f. Habitat span across all three realms.** Annelids occur in marine, freshwater and terrestrial systems, from hydrothermal vents and whale falls to soils and glaciers ([Britannica: annelid](https://www.britannica.com/animal/annelid); [Animal Diversity Web: Annelida](https://animaldiversity.org/accounts/Annelida/)). This is the property that specifically defeats `ENVO:01001176`.

**Sibling contrast (my inference, marked as such):** relative to `cnidarian-associated environment`, `sponge-associated environment` (requested) and `nematode-associated environment` (requested), the annelid concept is distinguished by the combination of a segmented coelomate body with metameric nephridia, a through-gut, and repeated independent origins of chemosynthetic endosymbiosis in three different compartments. No single source states this comparison; each component claim is cited above.

**Scale caveat.** Described-species totals for Annelida are unstable and source-dependent — commonly cited figures range from ~17,000 to >22,000, and differ precisely because of the circumscription question in §1.4. WoRMS's Annelida page does not publish a phylum-level accepted-species total. **Do not put a species count in the definition.**

---

## 4. Sources

Primary and standards sources for every claim above:

- Struck TH et al. (2011) Phylogenomic analyses unravel annelid evolution. *Nature* 471:95–98. [doi:10.1038/nature09864](https://doi.org/10.1038/nature09864) · PMID [21368831](https://pubmed.ncbi.nlm.nih.gov/21368831/) — circumscription of Annelida.
- Bright M, Giere O (2005) Microbial symbiosis in Annelida. *Symbiosis* 38:1–45. [full text PDF](https://dalspace.library.dal.ca/bitstream/handle/10222/78095/VOLUME%2038-NUMBER%201-2005-PAGE%201.pdf) — the one phylum-wide review of annelids as microbial habitat; the single best citation for the term request.
- Drake HL, Horn MA (2007) As the worm turns: the earthworm gut as a transient habitat for soil microbial biomes. *Annu Rev Microbiol* 61:169–189. [doi:10.1146/annurev.micro.61.080706.093139](https://doi.org/10.1146/annurev.micro.61.080706.093139) · PMID [17506687](https://pubmed.ncbi.nlm.nih.gov/17506687/).
- Horn MA, Schramm A, Drake HL (2003) The earthworm gut: an ideal habitat for ingested N₂O-producing microorganisms. *Appl Environ Microbiol* 69:1662–1669. [doi:10.1128/AEM.69.3.1662-1669.2003](https://doi.org/10.1128/AEM.69.3.1662-1669.2003) · PMID [12620857](https://pubmed.ncbi.nlm.nih.gov/12620857/) — the anoxia / pH 6.9 / C:N 7 measurements.
- Dubilier N et al. (2001) Endosymbiotic sulphate-reducing and sulphide-oxidizing bacteria in an oligochaete worm. *Nature* 411:298–302. [doi:10.1038/35077067](https://doi.org/10.1038/35077067).
- Woyke T et al. (2006) Symbiosis insights through metagenomic analysis of a microbial consortium. *Nature* 443:950–955. [doi:10.1038/nature05192](https://doi.org/10.1038/nature05192).
- Kleiner M et al. (2012) Metaproteomics of a gutless marine worm and its symbiotic microbial community. *PNAS* 109:E1173–E1182. [doi:10.1073/pnas.1121198109](https://doi.org/10.1073/pnas.1121198109).
- Hinzke T et al. (2021) Bacterial symbiont subpopulations have different roles in a deep-sea symbiosis. *eLife* 10:e58371. [https://elifesciences.org/articles/58371](https://elifesciences.org/articles/58371); and Hinzke T et al. (2019) Host–microbe interactions in the chemosynthetic *Riftia pachyptila* symbiosis. *mBio* 10:e02243-19. [doi:10.1128/mBio.02243-19](https://doi.org/10.1128/mBio.02243-19).
- Martínez-Redondo GI et al. (2023) Distinct genomic routes underlie transitions to specialised symbiotic lifestyles in deep-sea annelid worms. *Nat Commun* 14:2814. [doi:10.1038/s41467-023-38521-6](https://doi.org/10.1038/s41467-023-38521-6).
- Verna C et al. (2010) High symbiont diversity in the bone-eating worm *Osedax mucofloris*. *Environ Microbiol* 12:2355–2370. [doi:10.1111/j.1462-2920.2010.02299.x](https://doi.org/10.1111/j.1462-2920.2010.02299.x). Epibiont dynamics: Goffredi SK et al. (2023) A dynamic epibiont community associated with *Osedax*. PMID [37382438](https://pubmed.ncbi.nlm.nih.gov/37382438/).
- Haddad A et al. (1995) *Appl Environ Microbiol* 61:1679–1687 [doi:10.1128/aem.61.5.1679-1687.1995](https://doi.org/10.1128/aem.61.5.1679-1687.1995); Cary SC et al. (1997) *Appl Environ Microbiol* 63:1124–1130 [doi:10.1128/aem.63.3.1124-1130.1997](https://doi.org/10.1128/aem.63.3.1124-1130.1997); Tasiemski A et al. (2014) *PLOS ONE* 9:e95737 [doi:10.1371/journal.pone.0095737](https://doi.org/10.1371/journal.pone.0095737) — *Alvinella* epibionts and alvinellacin.
- Maltz M, Graf J (2012) Bacterial symbioses of the medicinal leech *Hirudo verbana*. *Gut Microbes* 3:322–331. [doi:10.4161/gmic.20227](https://doi.org/10.4161/gmic.20227); Ott BM et al. (2021) *Macrobdella decora*: Old World leech gut microbial community structure conserved in a New World leech. *Appl Environ Microbiol* [doi:10.1128/AEM.02082-20](https://doi.org/10.1128/AEM.02082-20).
- Lund MB et al. (2010) Beneficial effect of *Verminephrobacter* nephridial symbionts on earthworm fitness. *Appl Environ Microbiol* 76:4738–4743. [doi:10.1128/AEM.00108-10](https://doi.org/10.1128/AEM.00108-10) · [PMC2901725](https://pmc.ncbi.nlm.nih.gov/articles/PMC2901725/); review: [PMC3975124](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3975124/); Møller PR et al. (2018) *FEMS Microbiol Ecol* 94:fix178 [doi:10.1093/femsec/fix178](https://academic.oup.com/femsec/article/94/2/fix178/4768062); biparental transmission: [*FEMS Microbiol Ecol* 93:fix025 (2017)](https://academic.oup.com/femsec/article/93/5/fix025/3045886).
- Adomako MO, Wu J, Yu F-H (2025) Ecological and evolutionary responses of earthworm holobionts to environmental changes. *ISME J* 19:wraf044. [doi:10.1093/ismejo/wraf044](https://doi.org/10.1093/ismejo/wraf044) · PMID [40057975](https://pubmed.ncbi.nlm.nih.gov/40057975/) — most recent synthesis treating the earthworm as a holobiont/habitat.
- Compartment structure of the drilosphere: Zhang et al. (2023) *Pedosphere* [S1002016023001108](https://www.sciencedirect.com/science/article/abs/pii/S1002016023001108); soil–plant–earthworm microniches, *Eur J Soil Biol* (2023) [S1164556323000675](https://www.sciencedirect.com/science/article/abs/pii/S1164556323000675).
- Standards: MIxS host-associated extension, Genomic Standards Consortium — `host_taxid` (NCBI taxon id), `host_body_habitat`, `host_body_site` (UBERON for animals) — [genomicsstandardsconsortium.github.io/mixs/0016002/](https://genomicsstandardsconsortium.github.io/mixs/0016002/); MIxS-SA symbiont-associated extension, *ISME Commun* 2022 [doi:10.1038/s43705-022-00092-w](https://www.nature.com/articles/s43705-022-00092-w). These are the reason a host-clade habitat term is needed at all: MIxS records the host as a taxid and the site as anatomy, with nothing in between naming the *environment* the host constitutes.
- Ontology terms verified live against EBI OLS4 on 2026-08-17: `ENVO:01001000`, `ENVO:01001001`, `ENVO:01001002`, `ENVO:01001041`, `ENVO:01001055`, `ENVO:01001111`, `ENVO:01001176`, `ENVO:01001179`, `ENVO:01000165`, `NCBITaxon:6340`, `AGRO:00002042`, `AGRO:00002043`. [OLS4](https://www.ebi.ac.uk/ols4/).
- WoRMS Annelida, AphiaID 882 — [marinespecies.org](https://www.marinespecies.org/aphia.php?p=taxdetails&id=882).

**Flagged as preprint, not peer-reviewed:** "Repeated losses and gains of bacterial symbionts in gutless marine annelids over 150 million years," [bioRxiv 10.1101/2021.04.28.441735](https://doi.org/10.1101/2021.04.28.441735). Do not cite it in a term request without checking for a published version.

**Flagged as my inference, not sourced:** (i) the sibling-contrast paragraph in §3; (ii) the recommendation that casts fall outside this concept despite GOLD nesting them inside it — the cited studies establish that cast communities differ from gut communities, but no source rules on the ontological question; (iii) the reading that GOLD's `Annelida` node means the whole living worm — well supported by the subtree shape, but GOLD publishes no definition for the node.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**

- Annelida (the GOLD node label)
- annelid host; annelid-associated
- segmented worm; bristle worm (Polychaeta, informally extended to the phylum)
- polychaete-associated / oligochaete-associated / earthworm-associated / leech-associated / tubeworm-associated — all **narrower**, each denoting a subclade; usable as narrow synonyms only, never exact
- "worm" in sample metadata, where the host is known to be an annelid

Suggested `exact_synonym` for the term request: `Annelida|annelid host|segmented worm-associated environment`.

**Commonly but wrongly treated as the same thing**

| Confusable | Why it is different |
|---|---|
| **Nematoda** ("roundworm," "worm") | A different phylum; HabitatMech already holds it as `habitatmech:GOLD.45a8229be1` with its own pending `nematode-associated environment` request. The commonest single conflation in host metadata. |
| **Platyhelminthes** ("flatworm"), Priapulida, Nemertea, Sipuncula-as-separate-phylum | Sipuncula is *inside* Annelida on current evidence ([Struck 2011](https://doi.org/10.1038/nature09864)); the others are not. |
| **Insect larvae** ("grubs," "worms") | Arthropoda; `Host-associated > Arthropoda > Insects` in GOLD. |
| **`NCBITaxon:6340` Annelida** | The taxon, not the habitat. Keep as `xref`. |
| **Vermicompost / worm castings** (`AGRO:00002042`, `AGRO:00002043`) | An engineered soil amendment; GOLD itself files "Vermicompost" under `Engineered > Solid waste`, i.e. a different top-level category. |
| **Drilosphere / earthworm burrow / burrow lining** | Worm-modified *soil*. A soil environment, not a host-associated one. |
| **`ENVO:01001111` fossil worm burrow** | A fossilised geological channel. |
| **Trophosome (`ENVO:01000165`)** | An organ of one annelid family; already a separate, correctly-grounded record. |
| **The vent / whale-fall / seep environment** | Where the worm lives, not what the worm is. |
| **"Host-associated > Invertebrates"** | The GOLD parent-ish bucket; broader and heterogeneous. |

---

## 6. Should it be a term at all?

**Yes.** Three independent reasons:

1. **It is a place, not a taxon.** The microorganisms in question live *in* the annelid — in its gut lumen, its nephridia, its coelom, under its cuticle, inside its bacteriocytes. Every claim in §3 is a claim about a physical setting with measurable properties (pH 6.9, anoxic, C:N 7; 10⁹ symbiont cells g⁻¹; >95% two-species dominance). The curation note's reversal of the earlier NOT_APPLICABLE is correct, and the physicochemical measurements are the concrete evidence for it.

2. **ENVO has no term and has already accepted the pattern.** `cnidarian-associated environment` (`ENVO:01001179`) is a phylum-level host-clade child of `ENVO:01001002` with the exact definitional shape proposed here. The near-misses in §2.3 all fail for stated reasons.

3. **It carries real data.** 150 GOLD organism assertions at the node itself, plus a 23-path anatomical subtree beneath it, all of which needs a coherent parent. Merging it into `ENVO:01001002` would collapse annelids with mammals, birds, fish and insects and lose the distinction GOLD is making.

**§6.1 — Do not over-claim in the definition.** Do not write in "chemosynthetic symbiosis" or "anoxic gut" as if they characterised the phylum: the trophosome symbiosis is Siboglinidae-only, the gutless consortium is Phallodrilinae-only, and the two-species crop is Hirudinida-only. The one property true of the whole concept is *the host is an annelid*. That is why the proposed sentence carries only the clade, with the rest as supporting material.

**§6.2 — Do not enumerate subclades in the definition.** The circumscription is under active revision (§1.4). An enumeration will need editing; "an annelid (phylum Annelida, NCBITaxon:6340)" will not. The enumeration in the proposed sentence above is deliberately illustrative ("whether … or …") rather than exhaustive; a curator preferring the strict ENVO house style should cut it and use "An environmental system determined by an annelid."

**§6.3 — One defect to fix regardless of the term request.** The record carries `parent_habitats: [ENVO:01001000]` (*environmental system determined by an organism*), while the curation note says "Nearest broader term NCBITaxon:6340 'Annelida' attached as a parent" — the note describes a parent the record does not have, and the parent the record does have is two levels too broad, sitting above the plant/animal/fungus split. Every sibling term request in `curation/term_requests.tsv` uses `ENVO:01001002` as `parent_class`. **Recommendation:** re-parent to `ENVO:01001002` *animal-associated environment* and keep `NCBITaxon:6340` where it already correctly is, in `xrefs`. This is a seeder/decision change, not a hand-edit.

**§6.4 — Suggested term-request row** (for `curation/term_requests.tsv`, if the curator accepts):

| field | value |
|---|---|
| `identifier` | `habitatmech:GOLD.6e10201167` |
| `requested_label` | `annelid-associated environment` |
| `parent_class` | `ENVO:01001002` |
| `parent_label` | `animal-associated environment` |
| `definition` | `An environmental system determined by an annelid.` |
| `exact_synonym` | `Annelida\|annelid host\|segmented worm-associated environment` |
| `notes` | Host clade is the entire content of the concept; GOLD hangs a 23-path anatomical subtree (digestive system, crop, nephridia, coelom, trophosome, cuticle, subcuticular space, gills, egg capsule) off it. Not grounded to the parent, because every clade would merge onto one record. ENVO already has this exact shape at `ENVO:01001179` cnidarian-associated environment. `ENVO:01001176` (aquatic invertebrate) is not a match: it asserts an aquatic habitat that terrestrial earthworms and leeches do not have. Phylum-wide review: Bright & Giere 2005, *Symbiosis* 38:1–45. |

## Citations

1. https://doi.org/10.1146/annurev.micro.61.080706.093139
2. https://dalspace.library.dal.ca/bitstream/handle/10222/78095/VOLUME%2038-NUMBER%201-2005-PAGE%201.pdf
3. https://www.sciencedirect.com/science/article/abs/pii/S1164556323000675
4. https://www.sciencedirect.com/science/article/abs/pii/S1002016023001108
5. https://doi.org/10.1038/nature09864
6. https://pubmed.ncbi.nlm.nih.gov/21368831/
7. https://www.marinespecies.org/aphia.php?p=taxdetails&id=882
8. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
9. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3975124/
10. https://academic.oup.com/femsec/article/94/2/fix178/4768062
11. https://doi.org/10.1128/AEM.00108-10
12. https://doi.org/10.1128/AEM.69.3.1662-1669.2003
13. https://pubmed.ncbi.nlm.nih.gov/12620857/
14. https://doi.org/10.1016/j.tim.2006.06.009
15. https://doi.org/10.4161/gmic.20227
16. https://doi.org/10.1128/AEM.02082-20
17. https://elifesciences.org/articles/58371
18. https://doi.org/10.1128/mBio.02243-19
19. https://doi.org/10.1038/35077067
20. https://doi.org/10.1038/nature05192
21. https://doi.org/10.1073/pnas.1121198109
22. https://doi.org/10.1101/2021.04.28.441735
23. https://doi.org/10.1111/j.1462-2920.2010.02299.x
24. https://doi.org/10.1038/s41467-023-38521-6
25. https://doi.org/10.1128/aem.61.5.1679-1687.1995
26. https://doi.org/10.1128/aem.63.3.1124-1130.1997
27. https://doi.org/10.1371/journal.pone.0095737
28. https://www.britannica.com/animal/annelid
29. https://animaldiversity.org/accounts/Annelida/
30. https://pubmed.ncbi.nlm.nih.gov/17506687/
31. https://pubmed.ncbi.nlm.nih.gov/37382438/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC2901725/
33. https://academic.oup.com/femsec/article/93/5/fix025/3045886
34. https://doi.org/10.1093/ismejo/wraf044
35. https://pubmed.ncbi.nlm.nih.gov/40057975/
36. https://genomicsstandardsconsortium.github.io/mixs/0016002/
37. https://www.nature.com/articles/s43705-022-00092-w
38. https://www.ebi.ac.uk/ols4/