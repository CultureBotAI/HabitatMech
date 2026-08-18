---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T05:21:29.887271'
end_time: '2026-08-18T05:34:57.353147'
duration_seconds: 807.47
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Air sacs
  habitat_identifier: habitatmech:GOLD.3982893194
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Insects > Respiratory system
    > Trachea > Air sacs'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Sibling-path\
    \ review (#12): grounding the bird 'Air sacs' concept made this one's sweep stale,\
    \ but UBERON's air sacs are ALL vertebrate \u2014 UBERON:0009060 is defined as\
    \ extensions of the lungs of birds, and every sibling term is avian or cetacean.\
    \ The path is Insects > Respiratory system > Trachea, where an air sac is a tracheal\
    \ dilation. UBERON has no insect air sac. Path: Host-associated > Arthropoda:\
    \ Insects > Respiratory system > Trachea > Air sacs (source concept habitatmech:GOLD.3982893194)"
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
  web_search_requests: 25
  num_turns: 49
  total_cost_usd: 5.444080500000001
  session_id: d8bc0cf8-d262-4ba3-8520-9f372969b67e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 25
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Air sacs
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.3982893194
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Insects > Respiratory system > Trachea > Air sacs
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Sibling-path review (#12): grounding the bird 'Air sacs' concept made this one's sweep stale, but UBERON's air sacs are ALL vertebrate — UBERON:0009060 is defined as extensions of the lungs of birds, and every sibling term is avian or cetacean. The path is Insects > Respiratory system > Trachea, where an air sac is a tracheal dilation. UBERON has no insect air sac. Path: Host-associated > Arthropoda: Insects > Respiratory system > Trachea > Air sacs (source concept habitatmech:GOLD.3982893194)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Air sacs** as a microbial habitat, with citations.

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

# Air sacs (`habitatmech:GOLD.3982893194`) — novel-term definition research

> **A dilated, thin‑walled region of an insect trachea in which the taenidia are reduced or absent, so that it is readily compressible and holds a reservoir of air within the insect's tracheal system.**

Genus: `UBERON:0003127` *open tracheal system trachea* ("A respiratory airway that is part of an open tracheal system"; exact synonym *invertebrate trachea*) — present in the vendored slice. Differentia: dilation + reduced/absent taenidia + compressibility + reservoir function.

If a curator prefers a genus that does not commit to air sacs *being* tracheae (see §2 for why that is contestable at the margins), the alternative one-sentence form is: *A part of an insect tracheal system which is a dilated, thin-walled, air-filled sac with taenidia reduced or absent, rendering it readily compressible.* That requires no intermediate class, but it groups under `BTO:0003870` *insect tracheal system* rather than a UBERON anatomical class.

---

## 1. What the concept denotes

**The reading the data means.** GOLD's ecosystem classification is a fixed five-level path (Ecosystem → Ecosystem Category → Ecosystem Type → Ecosystem Subtype → Specific Ecosystem) ([Mukherjee et al. 2021, *NAR* 49:D723–D733](https://academic.oup.com/nar/article/49/D1/D723/5957166); [GOLD v.9, Mukherjee et al. 2023, PMID 36318257](https://pubmed.ncbi.nlm.nih.gov/36318257/)). This record's path fills all five: Host-associated / **Arthropoda: Insects** / Respiratory system / **Trachea** / Air sacs. So the concept is unambiguously the *insect tracheal air sac* — the specific ecosystem is a subdivision of the insect trachea, not a lung derivative. The curator's existing note reads this correctly.

**The physical place.** An air sac is an enlarged, thin-walled, **air-filled** compartment of the insect's open tracheal system: an ectodermal invagination lined by a chitinous intima (cuticle), continuous with the tracheae and, through them, with the outside atmosphere via spiracles. Harrison et al. define them as "enlarged, irregularly shaped structures connected to and developmentally derived from the tracheal system", whose "large size and reduced (or absent) taenidia … enable them to compress more easily in response to a pressure gradient than most tracheae" ([Harrison, McKenzie, Talal, Socha, Westneat & Matthews 2023, *J. Exp. Biol.* 226:jeb245712, doi:10.1242/jeb.245712](https://doi.org/10.1242/jeb.245712)). Snodgrass's classic formulation, quoted in the AMNH tracheal monograph, is simply that "air sacs … are enlarged tracheae" (Snodgrass 1935, *Principles of Insect Morphology*, cited in [Herhold, Davis, DeGrey & Grimaldi 2023, *Bull. AMNH* 459:1–184, doi:10.1206/0003-0090.459.1.1](https://digitallibrary.amnh.org/items/b17f33e1-0a31-4877-9ebc-b79b7f280de8)).

**A sample taken from this habitat** is therefore the dissected wall + lumen contents of a thoracic, abdominal, or cephalic air sac of an adult (usually) pterygote insect — a dry, cuticle-lined internal air space, not a fluid-filled or mucosal one.

**Boundary — what is inside the concept:**

- named air sacs of the head, thorax, legs, antennae and abdomen (in *Drosophila*: frontal head, antennal, propleural, sternopleural, hypopleural, pleural, postnotal, anteroscutal, dorsal and abdominal air sacs — `FBbt:00003101` and children);
- both morphological grades: "trachea-like sacs" (dilated but with widely spaced taenidia) and irregular sacs lacking taenidia (Harrison et al. 2023).

**Boundary — what is a neighbouring concept, not this one:**

- ordinary (non-dilated, taenidiate) **trachea** — the parent record `habitatmech:GOLD.2a2774b70a`;
- **tracheoles**, the blind-ending <1 µm terminal tubes that are the actual gas-exchange surface — a different, narrower compartment;
- **spiracles**, the gated body-wall openings — already grounded in this corpus to `UBERON:6005054` *insect spiracle*;
- the **haemocoel** on the other side of the tracheal epithelium — where entomopathogens end up after crossing, but a distinct habitat;
- the **honey sac / crop** of bees, which is a foregut structure, not respiratory (see §5).

**One genuine ambiguity, already resolved elsewhere in this corpus:** "Air sacs" is a cross-phylum homonym. GOLD carries a *second* "Air sacs" concept under Host-associated > Birds > Respiratory system, grounded to `UBERON:0009060` (decision on `habitatmech:GOLD.1dec05f10e`). The insect and avian structures are not homologous — avian air sacs are membranous extensions of the *lungs*; insect air sacs are dilations of *tracheae*. There is a third homonym in mammals (`UBERON:0013175` *nasal air sac*, a cetacean structure). The source path is decisive here and no silent choice is being made.

## 2. Genus — the broader kind

**Best available genus terms (all verified present in `data/raw/ontology_terms.tsv`):**

| CURIE | Label | Definition | Fit |
|---|---|---|---|
| `UBERON:0003127` | open tracheal system trachea | "A respiratory airway that is part of an open tracheal system." Synonyms: *invertebrate trachea*, *trachea* | **Recommended genus.** Broad, taxon-correct, asserts only "respiratory airway of an open tracheal system" |
| `UBERON:6005043` | insect trachea | "Cuticle-lined epithelial tube that forms part of the insect tracheal system." (`subClassOf UBERON:0003127`) | Good, but asserts *tube*, which is exactly what an irregular punctate sac is not |
| `BTO:0003870` | insect tracheal system | "The respiratory system of insects that consists of internal air-filled tubes." | Correct but is the whole *system*, i.e. too broad and of the wrong grain (system vs part) |
| `ENVO:01001055` | environment associated with an animal part or small animal | "An environmental system determined by part of a living or dead animal…" | The ENVO-side genus if the record is framed as an environment rather than an anatomical site; nothing insect- or respiratory-specific exists below it |

**ENVO was checked specifically.** ENVO's organism-determined environment branch in the vendored slice contains only `ENVO:01001000` (environmental system determined by an organism), `ENVO:01001001` plant-associated, `ENVO:01001002` animal-associated, `ENVO:01001041` fungi-associated and `ENVO:01001179` cnidarian-associated environment. **There is no insect-associated environment, no arthropod-associated environment, and no respiratory-tract environment in ENVO.** So ENVO cannot supply a genus more specific than "animal-associated".

**Near-misses worth recording (each fails, and why):**

- `UBERON:0009060` **air sac** — label-identical, and the trap this record already avoided. Its definition is "Any of the membranous air-filled extensions of the **lungs of birds**". Grounding here would assert lungs, birds, and homology that does not exist. Its whole subtree (`UBERON:0009061/0009062` anterior/posterior, `0009063` interclavicular, `0009064` cervical, `0009065/0009066` thoracic, `0009948` clavicular) is avian.
- `UBERON:0009067` **abdominal air sac** — a second-order trap. Insects also have an abdominal air sac (`FBbt:00003119`, "a distended region of the tracheal dorsal trunk in abdominal segments 1 and 2"), but UBERON's term is a child of `UBERON:0009062` *posterior air sac*, i.e. avian. Pure homonym.
- `UBERON:0013175` **nasal air sac** — cetacean, echolocation-associated.
- `UBERON:0003126` **trachea** — synonyms *windpipe*, *vertebrate trachea*; the vertebrate airway. This is the same homonym that `UBERON:6005054` *insect spiracle* was introduced to avoid for the sibling Spiracles record. **See the flag in §7 — the parent record currently uses this term.**
- `BTO:0000060` **alveolus** / `BTO:0003511` alveolar epithelium — vertebrate lung; functionally analogous to tracheoles, not to air sacs.
- `UBERON:0006860` **swim bladder** / `BTO:0002148` gas bladder — a gas-filled buoyancy organ, and insect air sacs do serve buoyancy in aquatic larvae, but the swim bladder is a vertebrate gut derivative. Not the same kind.
- `FBbt:00003101` **adult tracheal air sac** — *this is an exact conceptual match*: "Air filled epithelial sac of the adult tracheal system. These highly dilated trachea consist of thin epithelium with very thin chitinous lining, lacking taenidia. Consequently they are highly flexible and can collapse or expand with changes in pressure around them." It fails as a grounding target for two independent reasons: **(a)** FBbt is not in HabitatMech's grounding set (ENVO, UBERON, FOODON, BTO, PO) and is not in the vendored slice; **(b)** FBbt classes are *Drosophila melanogaster*-specific by construction, while GOLD's node is Insecta-wide. It is, however, the single best model for the definition text and strong evidence that a UBERON `6xxxxxx` insect-anatomy term would be uncontroversial — UBERON already carries that bridge branch (`UBERON:6005043`, `UBERON:6005054`, `UBERON:6003039`).

## 3. Differentia — what distinguishes it from its siblings

All of the following are attested; the first four are the definitional ones.

1. **Dilation.** The structure is an *enlarged* region of the tracheal system, not a tube of ordinary calibre (Harrison et al. 2023; Snodgrass 1935 via Herhold et al. 2023).
2. **Taenidia reduced or absent.** Taenidia are "ring-like thickenings of tracheal wall thought to reduce compressibility" (Harrison et al. 2023, Glossary). Their reduction is the observable, microscopy-checkable feature that separates an air sac from a trachea of the same diameter. Faucheux's three-way classification turns entirely on this: "(1) taenidial sacs, in which the general shape of the trachea is maintained but dilated, and regular taenidia are present but widely spaced; (2) reticulate sacs, with criss-crossing taenidia and irregular shapes; and (3) punctate sacs, with irregular shape and lacking taenidia" (Faucheux & Sellier 1971; Faucheux 1972, quoted verbatim in Harrison et al. 2023).
3. **Compressibility / reservoir function.** Thin epithelium and very thin chitinous lining make air sacs "highly flexible", able to "collapse or expand with changes in pressure around them" (`FBbt:00003101`); they act as bellows that increase tidal volume and drive advection (Wigglesworth 1963, *Nature*, as summarised by Harrison et al. 2023). Compression is measurable *in vivo* by synchrotron X-ray microtomography, and is **anisotropic**, not isotropic ([Iwan, Rühle & Betz 2016 / Wang et al., *Sci. Rep.* 6:32380, doi:10.1038/srep32380](https://www.nature.com/articles/srep32380) — see PMC5007674).
4. **Air-filled, cuticle-lined, atmosphere-connected lumen.** The tracheal system is "an air-filled tubular organ formed by invaginations of the ectoderm lined by a chitinous intima", and depending on species may occupy up to ~50% of total body volume ([Bossen, Kühle & Roeder 2023, *Insect Biochem. Mol. Biol.* 157:103960, doi:10.1016/j.ibmb.2023.103960](https://doi.org/10.1016/j.ibmb.2023.103960)). This is the physicochemical differentia that matters for microbiology: unlike the gut, this is a **dry, chitin-surfaced, near-atmospheric-PO₂** compartment rather than a wet, nutrient-rich, anoxic-to-microoxic one.
5. **Host constraint — taxon and life stage.** Presence of air sacs is not universal within Insecta and is a real constraint on what a sample labelled "air sacs" can be. Harrison et al. 2023 report that air sacs are absent in basal apterygote hexapods, absent or rare in Paleoptera, and widespread in Neoptera, with occurrence "closely associated with strong flight capacity (χ²=25.3, P<0.001)"; they are largest in strong fliers (Diptera, Hymenoptera, some Coleoptera) and tend to be absent in aquatic insects. They are also developmentally late: first instars of *Schistocerca americana* lack air sacs, which enlarge through the juvenile stages (Greenlee et al. 2009, cited in Harrison et al. 2023), and in *Drosophila* the dorsal air sacs are **adult** structures built at metamorphosis from the air sac primordium ([Yorozu & Guha, *Int. J. Mol. Sci.* 19:2074, doi:10.3390/ijms19072074](https://doi.org/10.3390/ijms19072074); [Manning & Krasnow / Hayashi & Kondo 2018, *Front. Insect Sci.*-adjacent review, PMC5972413](https://pmc.ncbi.nlm.nih.gov/articles/PMC5972413/)).

**Sibling separation under the genus, in one line each:** trachea = taenidiate, tubular, not dilated; tracheole = <1 µm, blind-ending, intracellular terminal, the actual exchange surface; spiracle = the gated opening through the body wall; air sac = dilated, taenidia-poor, compressible reservoir.

## 4. Evidence that this is a *microbial* habitat — and the honest limits

This is where the record is weakest, and a curator should know it before writing anything mechanistic.

**Nothing has been sequenced from this path.** Upstream assertion volume for `habitatmech:GOLD.3982893194` is **0**: no GOLD genome or metagenome carries this specific ecosystem. The term is an anatomical slot in GOLD's tree, not an attested sampling site.

**The insect tracheal system as a whole *is* a demonstrated microbial habitat.** The only direct study I found is [Angstmann, Pfeiffer, Kublik, Ehrhardt, Uliczka, Rabe, Roeder, Wagner, Schloter & Krauss-Etschmann 2023, "The microbial composition of larval airways from *Drosophila melanogaster* differ between specimens from laboratory and natural habitats", *Environmental Microbiome* 18:55, doi:10.1186/s40793-023-00506-9](https://doi.org/10.1186/s40793-023-00506-9) (PMID 37370177; PMC10303296). Tracheae were dissected under sterile conditions using only gas-filled (undamaged) tracheae, with non-template controls; 16S barcoding showed lab-strain larval airways dominated by Acetobacteraceae and Lactobacillaceae, and wild-caught larval airways by Lactobacillaceae, Anaplasmataceae (*Wolbachia* sp.) and Leuconostocaceae (*Weissella* sp.), with elevated *Serratia* in immune-deficient *relish*⁻ᐟ⁻ larvae. The authors' conclusion is that *Drosophila* larvae "harbor an airway microbiome of low complexity". **Caveat the curator must not lose: these are larvae, which do not have air sacs.** The finding licenses "the insect tracheal system hosts microbes"; it does not license "air sacs host a characteristic microbiome".

**Framing statements from the same group** are explicit that the question is open: for insects "it is unknown up to now whether the tracheal system harbors an indigenous microbiota" ([Roeder group review, *Front. Allergy* 3:876673, 2022, doi:10.3389/falgy.2022.876673](https://doi.org/10.3389/falgy.2022.876673)). The tracheal-immunity review notes that "many pathogens and parasites — including viruses, bacteria, fungi and metazoan parasites — colonize the trachea or invade the host via this route" (Bossen et al. 2023, doi:10.1016/j.ibmb.2023.103960).

**Air sacs specifically are attested as a colonised internal compartment — by metazoan parasites, not yet by characterised microbial communities.** The WOAH *Terrestrial Manual* chapter 3.2.1 (Acarapisosis of honey bees) states that *Acarapis woodi* lives and reproduces "mainly in the large prothoracic tracheae of the bee. Sometimes they are also found in the **head, thoracic and abdominal air sacs**" (citing Giordani 1965; Wilson et al. 1997), and describes the resulting melanised, opaque tracheal walls ([WOAH Terrestrial Manual, ch. 3.2.1](https://www.woah.org/fileadmin/Home/fr/Health_standards/tahm/3.02.01_ACARAPISOSIS.pdf)). For bumble bees, *Locustacarus buchneri* (Podapolipidae) completes its whole life cycle in the respiratory system, "usually the metasomal (abdominal) air sacs", of adult *Bombus* ([USDA/IDtools Bee Mite ID](https://idtools.org/bee_mite/index.cfm?packageID=1&entityID=116); [Plischuk, Meeus, Smagghe & Lange 2013, *J. Asia-Pacific Entomol.* 16:281–283](https://www.sciencedirect.com/science/article/abs/pii/S1383576913001074)).

**Fungal colonisation of the tracheal lumen is documented, though in tracheae rather than air sacs:** *Metarhizium anisopliae* in *Culex quinquefasciatus* larvae produced near-complete blockage of the trachea by mycelium beginning at the siphon, with appressoria and host melanisation, death attributed primarily to suffocation ([Route of Invasion and Histopathology of *Metarhizium anisopliae* in *Culex quinquefasciatus*](https://digitalcommons.usu.edu/biology_facpub/1399)). In terrestrial hosts tracheae are typically destroyed later, during general hyphal ramification through the haemocoel (e.g. *Lecanicillium lecanii* in *Phenacoccus fraxinus*, [PMC4309582](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4309582/); *M. anisopliae* in *Rhynchophorus ferrugineus*, [PMC5055524](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5055524/)).

**My inference, flagged as such:** that an air sac's habitat character — dry chitinous surface, near-atmospheric oxygen, direct spiracular connection to outside air, and a compressible volume flushed by ventilation — differs materially from the insect gut is an inference from the anatomy and physiology cited above, not a claim any single source makes about air sacs as a microbial niche. **Do not put a mechanism claim or a community description in the record.** Under this repo's rules a `causal_graphs` edge here would need evidence that does not exist.

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**

- *air sac* (the standard term; Snodgrass 1935 onward)
- *tracheal air sac* / *adult tracheal air sac* (`FBbt:00003101`)
- *taenidial sac*, *reticulate sac*, *punctate sac* — Faucheux's three morphological grades, all subsumed by "air sac" (Faucheux & Sellier 1971; Faucheux 1972)
- *trachea-like sac* — Harrison et al.'s (2023) name for the taenidiate grade
- regional names that are this concept at a finer grain: *dorsal air sac*, *abdominal air sac*, *frontal head air sac*, *propleural / sternopleural / hypopleural / pleural / postnotal / anteroscutal air sac* (FBbt)
- historically, *dilated trachea* / *enlarged trachea* (Snodgrass 1935)

**Do not conflate with**

| Wrongly treated as the same | Why it is different |
|---|---|
| **Avian air sac** (`UBERON:0009060`, and GOLD's own Birds > Respiratory system > Air sacs) | Extension of the *lungs* of birds; non-homologous; already a separate grounded record in this corpus |
| **Avian abdominal / thoracic air sac** (`UBERON:0009067`, `0009065`, `0009066`) | Label-identical to insect regional air sacs but sits under the avian `UBERON:0009060` |
| **Cetacean nasal air sac** (`UBERON:0013175`) | Blowhole-associated, echolocation-related |
| **Vertebrate trachea / windpipe** (`UBERON:0003126`) | Cartilage-ringed vertebrate airway; homonym of insect trachea |
| **Tracheole** | The gas-exchange terminal, <1 µm, blind-ending; opposite end of the size and function range |
| **Air sac primordium (ASP)** | The larval imaginal-tracheoblast bud that *becomes* an air sac; a developmental structure, not a habitat ([Yorozu & Guha 2018](https://doi.org/10.3390/ijms19072074)) |
| **Honey sac / crop** of bees | Foregut, not respiratory — a real confusion risk because the bee microbiome literature uses "honey sac" freely (e.g. [Front. Insect Sci. 2025, doi:10.3389/finsc.2025.1555434](https://www.frontiersin.org/journals/insect-science/articles/10.3389/finsc.2025.1555434/full)) |
| **Swim bladder / gas bladder** (`UBERON:0006860`, `BTO:0002148`) | Vertebrate gut derivative; convergent buoyancy function only |
| **"Tracheal mite" disease** (acarapisosis) | A disease/infestation state, not the habitat |

## 6. Should this be a term at all?

**Yes.** It passes every test this corpus applies:

- It is **a place, not a process, quality, disease or taxon** — a bounded, air-filled anatomical cavity from which a sample can be taken.
- It is **a host's part, not the whole host organism**, so the rule in CLAUDE.md that sends `Mollusca`/`larva`/`pupa` to a minted identity with an `xref` does not apply here; air sacs sit with `gut`, `skin`, `lung`, `blood` and the already-grounded `insect spiracle` as parts that ground to anatomy normally.
- **No term in ENVO, UBERON, FOODON, BTO or PO names it** (§2), which is exactly the condition for minting.
- A well-formed genus-differentia definition already exists for the *Drosophila* case (`FBbt:00003101`), which means the concept is not vague — it is simply unrepresented at Insecta rank in the ontologies HabitatMech uses.

**Recommended disposition (curator's call, but this is the shape I would argue for):** keep the minted identity `habitatmech:GOLD.3982893194`, and change the decision from bare `CONFIRM_UNGROUNDED` to **`GROUND_AS_PARENT UBERON:0003127 "open tracheal system trachea"`** — an air sac genuinely *is* a respiratory airway of an open tracheal system, so this satisfies the "`parent_habitats` means broader" rule rather than stretching it, and it gives the record the taxon-correct ancestor it currently lacks (it has no nearest broader term at all). Add `UBERON:6005043` *insect trachea* as `relation: xref` if a second link is wanted, and file a **UBERON term request for an insect air sac class** in the `UBERON:6xxxxxx` insect-anatomy branch, citing `FBbt:00003101` and Harrison et al. 2023 — the branch already contains `insect trachea`, `dorsal trunk of insect trachea` and `insect spiracle`, so the gap is an omission rather than a modelling objection.

One caution on the genus, stated plainly because it affects the wording: calling an air sac a *trachea* is standard (Snodgrass: "enlarged tracheae"; FBbt: "these highly dilated trachea") but slightly strained for Faucheux's punctate grade, which is irregular and taenidia-free. Harrison et al. handle this by treating tracheae and air sacs as "a continuum from ringed tracheae to" irregular sacs. The proposed definition uses "region of an insect trachea", which the continuum framing supports; a curator who wants zero exposure on that point should use the `BTO:0003870`-anchored alternative given at the top.

## 7. One defect found in a neighbouring record (worth an issue)

The parent record **`habitatmech:GOLD.2a2774b70a` "Trachea"** (`data/habitats/host_associated/trachea__4ac9ebc1.yaml`, path *Host-associated > Arthropoda: Insects > Respiratory system > Trachea*) is `mapping_status: SEEDED`, `grounding_status: NARROW`, with `parent_habitats: [UBERON:0003126, …]`. `UBERON:0003126` is the **vertebrate windpipe** ("the portion of the airway that attaches to the bronchi"; synonyms *windpipe*, *vertebrate trachea*). This is precisely the cross-phylum homonym that decision `habitatmech:GOLD.7ee93ccae2` caught and fixed for Spiracles by using `UBERON:6005054` *insect spiracle*. Both correct targets are already in the vendored slice: `UBERON:0003127` *open tracheal system trachea* (synonym *invertebrate trachea*) and `UBERON:6005043` *insect trachea*. Since this air sac record's only parent is that record, the error propagates: the insect air sac currently inherits, transitively, from the human windpipe. This is unreviewed seeder output, not a curation decision, so it should be a separate issue and a separate decision row rather than something folded into the air-sac definition.

---

### Sources

- Harrison, J.F., McKenzie, E.K.G., Talal, S., Socha, J.J., Westneat, M.W. & Matthews, P.G.D. (2023). Air sacs are a key adaptive trait of the insect respiratory system. *J. Exp. Biol.* 226(10):jeb245712. https://doi.org/10.1242/jeb.245712 · [PubMed 37204298](https://pubmed.ncbi.nlm.nih.gov/37204298/) · [open PDF](https://par.nsf.gov/servlets/purl/10628134)
- Herhold, H.W., Davis, S.R., DeGrey, S.P. & Grimaldi, D.A. (2023). Comparative anatomy of the insect tracheal system, part 1. *Bull. Am. Mus. Nat. Hist.* 459:1–184. https://doi.org/10.1206/0003-0090.459.1.1 · [free full text, AMNH](https://digitallibrary.amnh.org/items/b17f33e1-0a31-4877-9ebc-b79b7f280de8)
- Bossen, J., Kühle, J.-P. & Roeder, T. (2023). The tracheal immune system of insects — a blueprint for understanding epithelial immunity. *Insect Biochem. Mol. Biol.* 157:103960. https://doi.org/10.1016/j.ibmb.2023.103960
- Angstmann, H., Pfeiffer, S., Kublik, S. et al. (2023). The microbial composition of larval airways from *Drosophila melanogaster* differ between specimens from laboratory and natural habitats. *Environmental Microbiome* 18:55. https://doi.org/10.1186/s40793-023-00506-9 · [PMC10303296](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10303296/)
- Roeder group (2022). Airway remodeling: the *Drosophila* model permits a purely epithelial perspective. *Front. Allergy* 3:876673. https://doi.org/10.3389/falgy.2022.876673
- Bossen, J. et al. (2025). Chronic airway inflammation in *Drosophila* lacking the A20-like protein Trabid. *Front. Immunol.* 16:1564386. https://doi.org/10.3389/fimmu.2025.1564386
- Yorozu, S. & Guha, A. (2018). The air sac primordium of *Drosophila*: a model for invasive development. *Int. J. Mol. Sci.* 19:2074. https://doi.org/10.3390/ijms19072074 · [PMC6073991](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6073991/)
- Development and function of the *Drosophila* tracheal system (2018). [PMC5972413](https://pmc.ncbi.nlm.nih.gov/articles/PMC5972413/)
- Anisotropic shrinkage of insect air sacs revealed *in vivo* by X-ray microtomography. *Sci. Rep.* 6:32380 (2016). https://doi.org/10.1038/srep32380 · [PMC5007674](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5007674/)
- WOAH (OIE) *Terrestrial Manual*, ch. 3.2.1, Acarapisosis of honey bees. https://www.woah.org/fileadmin/Home/fr/Health_standards/tahm/3.02.01_ACARAPISOSIS.pdf
- USDA/IDtools Bee Mite ID — *Locustacarus*. https://idtools.org/bee_mite/index.cfm?packageID=1&entityID=116 · Plischuk, S. et al. (2013). The tracheal mite *Locustacarus buchneri* in South American native bumble bees. *J. Asia-Pacific Entomol.* https://www.sciencedirect.com/science/article/abs/pii/S1383576913001074
- Route of invasion and histopathology of *Metarhizium anisopliae* in *Culex quinquefasciatus*. https://digitalcommons.usu.edu/biology_facpub/1399
- Mukherjee, S. et al. (2021). Genomes OnLine Database (GOLD) v.8. *Nucleic Acids Res.* 49:D723–D733. https://academic.oup.com/nar/article/49/D1/D723/5957166 · GOLD v.9 (2023), [PMID 36318257](https://pubmed.ncbi.nlm.nih.gov/36318257/)
- Ontology terms verified live via EBI OLS4 (`UBERON:0003127`, `UBERON:6005043`, `UBERON:0009060`, `UBERON:0009067`, `UBERON:0013175`, `BTO:0003870`, `ENVO:01001002`, `ENVO:01001055`, `FBbt:00003101`) and cross-checked against this repo's vendored slice `data/raw/ontology_terms.tsv`.

## Citations

1. https://academic.oup.com/nar/article/49/D1/D723/5957166
2. https://pubmed.ncbi.nlm.nih.gov/36318257/
3. https://doi.org/10.1242/jeb.245712
4. https://digitallibrary.amnh.org/items/b17f33e1-0a31-4877-9ebc-b79b7f280de8
5. https://www.nature.com/articles/srep32380
6. https://doi.org/10.1016/j.ibmb.2023.103960
7. https://doi.org/10.3390/ijms19072074
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC5972413/
9. https://doi.org/10.1186/s40793-023-00506-9
10. https://doi.org/10.3389/falgy.2022.876673
11. https://www.woah.org/fileadmin/Home/fr/Health_standards/tahm/3.02.01_ACARAPISOSIS.pdf
12. https://idtools.org/bee_mite/index.cfm?packageID=1&entityID=116
13. https://www.sciencedirect.com/science/article/abs/pii/S1383576913001074
14. https://digitalcommons.usu.edu/biology_facpub/1399
15. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4309582/
16. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5055524/
17. https://www.frontiersin.org/journals/insect-science/articles/10.3389/finsc.2025.1555434/full
18. https://pubmed.ncbi.nlm.nih.gov/37204298/
19. https://par.nsf.gov/servlets/purl/10628134
20. https://doi.org/10.1206/0003-0090.459.1.1
21. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10303296/
22. https://doi.org/10.3389/fimmu.2025.1564386
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6073991/
24. https://doi.org/10.1038/srep32380
25. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5007674/