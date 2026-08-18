---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T04:04:33.551082'
end_time: '2026-08-18T04:13:00.609318'
duration_seconds: 507.06
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Gaster
  habitat_identifier: habitatmech:GOLD.623ff8e506
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Arthropoda: Insects > Abdomen > Metasoma
    > Gaster'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Disjoint-grounding
    review (#62): was UBERON:0000945 ''stomach'', a vertebrate organ. The path is
    Arthropoda: Insects > Abdomen > Metasoma > Gaster, and an insect gaster is a region
    of the abdomen rather than a stomach. Path: Host-associated > Arthropoda: Insects
    > Abdomen > Metasoma > Gaster (source concept habitatmech:GOLD.623ff8e506)'
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
  web_search_requests: 12
  num_turns: 26
  total_cost_usd: 2.6163499999999993
  session_id: 330e017e-8ff9-4b6a-adf0-6b24152b0d1b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 30
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Gaster
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.623ff8e506
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Arthropoda: Insects > Abdomen > Metasoma > Gaster
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Disjoint-grounding review (#62): was UBERON:0000945 'stomach', a vertebrate organ. The path is Arthropoda: Insects > Abdomen > Metasoma > Gaster, and an insect gaster is a region of the abdomen rather than a stomach. Path: Host-associated > Arthropoda: Insects > Abdomen > Metasoma > Gaster (source concept habitatmech:GOLD.623ff8e506)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Gaster** as a microbial habitat, with citations.

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

# Gaster — novel-term research for `habitatmech:GOLD.623ff8e506`

## Proposed definition

> An animal-associated environment which consists of the gaster of an apocritan hymenopteran — the bulbous posterior body region formed by all abdominal segments behind the petiole — together with the crop, midgut, hindgut, glandular and reproductive tissues it encloses, sampled as an intact body region rather than as dissected organs.

**Caveat the curator should weigh before adopting this sentence.** The genus above is two levels broader than it should be. ENVO has no `insect-associated environment`, no `arthropod-associated environment`, and no `metasoma environment`; `animal-associated environment` (ENVO:01001002) has exactly three asserted children — `environment associated with an aquatic invertebrate` (ENVO:01001176), `cnidarian-associated environment` (ENVO:01001179), and `human settlement` (ENVO:01001829) — none of which is on the path to an insect body region. The missing intermediate classes are the real finding here; see §2 and §6.

---

## 1. What the concept denotes

**The reading the data means.** The source path is `Host-associated > Arthropoda: Insects > Abdomen > Metasoma > Gaster` (GOLD ecosystem path, `gold.ecosystem:7252`, depth 5). That path is unambiguous: it is entomological anatomy, nested under insect abdomen and under metasoma. The concept is the **gaster of an apocritan hymenopteran** — an ant, bee, or wasp — treated as the physical body region a microbiological sample is taken from.

**Boundaries — what is inside.** The gaster is the bulbous posterior portion of the metasoma in Apocrita, comprising the abdominal segments posterior to abdominal segment 2 ([HAO:0000369](https://www.ebi.ac.uk/ols4/ontologies/hao/classes?obo_id=HAO:0000369); [Bolton's terminology as summarised on AntWiki](https://www.antwiki.org/wiki/Morphological_Terms/Worker_Metasoma)). In most ants it begins at abdominal segment III; where segment III is constricted into a postpetiole, the gaster begins at segment IV. It bears 5–7 visible tergites and matching sternites.

As a habitat, the enclosed contents are what matter, and they are heterogeneous:

- **Foregut-derived crop ("social stomach")** and the **proventriculus** valve. Although foregut in origin, both sit *inside* the gaster: in *Camponotus pennsylvanicus* the crop, proventriculus, and ventriculus "lie practically on the floor of the first three gastral segments," the oesophagus reaching them by passing through the waist ([Eisner & Brown 1958 anatomy, as reproduced in the ant digestive-anatomy literature](https://www.researchgate.net/figure/a-f-Digestive-anatomy-of-ants-a-Proventriculus-pv-in-the-context-of-the-digestive_fig1_8666351); [AntWiki, Trophallaxis](https://www.antwiki.org/wiki/Trophallaxis)).
- **Midgut**, in Camponotini studded with bacteriocytes housing *Candidatus* Blochmannia ([Sauer et al. 2002, AEM 68:4187–4193](https://pubmed.ncbi.nlm.nih.gov/12200266/); [Stoll et al. 2010, BMC Microbiol 10:308, doi:10.1186/1471-2180-10-308](https://bmcmicrobiol.biomedcentral.com/articles/10.1186/1471-2180-10-308)).
- **Ileum and rectum**, Malpighian tubules, fat body.
- **Reproductive tissues** — ovaries/oocytes, a *Wolbachia* and *Blochmannia* niche and the route of vertical transmission ([Sauer et al. 2002](https://pubmed.ncbi.nlm.nih.gov/12200266/); [Ramalho et al. on transovarian transmission in *Camponotus textor*](https://www.wikidata.org/wiki/Q50422384)).
- **Exocrine glands and the sting apparatus** — poison (venom) gland, Dufour's gland, and in Formicinae the acidopore at the gaster tip ([Tragust et al. 2020, eLife 9:e60287, doi:10.7554/eLife.60287](https://elifesciences.org/articles/60287)).
- **The gastral cuticle surface**, which is why whole-gaster protocols surface-sterilize before extraction (see §3).

**Boundaries — what is a neighbouring concept, not this one.**

| Neighbour | Why it is outside |
|---|---|
| **Propodeum** (abdominal segment I) | Fused to the thorax; part of the *mesosoma*, not the metasoma ([AntWiki](https://www.antwiki.org/wiki/Morphological_Terms/Worker_Metasoma)) |
| **Petiole** (A2) and **postpetiole** (A3) | Part of the metasoma but explicitly *not* the gaster; they are the parent concept's remainder |
| **Metasoma** (parent record `habitatmech:GOLD.93f0f7b66d`) | Broader: metasoma = petiole + postpetiole + gaster |
| **Gut / digestive tract** | Narrower and only one of several tissue systems inside the gaster |
| **Head / mesosoma structures** — infrabuccal pocket, metapleural gland, thoracic crop | Different tagma; the infrabuccal pocket in particular is a mouthpart filter, not gastral ([AntWiki](https://www.antwiki.org/wiki/Trophallaxis)) |

**Is the label ambiguous?** Yes, in exactly one way, and it is the way that already caused a wrong grounding on this record. In Latin anatomical nomenclature *gaster* means **stomach**: `UBERON:0000945` *stomach* and `BTO:0001307` *stomach* both carry "gaster" as a related synonym, and `UBERON:0001199` *mucosa of stomach* carries "tunica mucosa (gaster)" (verified via [OLS4 exact-synonym search](https://www.ebi.ac.uk/ols4/api/search?q=gaster&exact=true)). The GOLD path rules that reading out. Outside Apocrita there is no third reading in play — "gaster" is not standard for the abdomen of non-apocritan insects.

---

## 2. Genus — the broader kind

**Nothing in ENVO, UBERON, FOODON, BTO or PO expresses this concept, and nothing expresses its immediate genus either.** Near-misses, each with the reason it fails:

| Candidate | Verdict |
|---|---|
| **ENVO:01001002** *animal-associated environment* — "An environmental system determined by an animal" ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)) | **Usable but far too broad.** It is determined by *an animal*, i.e. the whole host; it makes no claim about a body region. It is the only ENVO ancestor available, so it is the working genus by default, not by fit. |
| **ENVO:01001033** *digestive tract environment* — "An environmental system which has its properties and dynamics determined by a digestive tract" | **Narrower than the concept.** The gaster contains the digestive tract *plus* fat body, ovaries, glands and cuticle. Grounding here would silently restrict the concept to gut samples — precisely the distinction the whole-gaster vs. dissected-compartment literature insists on (§3). Its only body-part-specific child is **ENVO:01001187** *holothurian digestive tract*, which shows the intended pattern but has no insect analogue. |
| **ENVO:01001176** *environment associated with an aquatic invertebrate* | Wrong branch — the hosts here are terrestrial insects. |
| **UBERON:0000916** *abdomen* | **Explicitly excluded by taxon.** Its definition reads "The subdivision of the **vertebrate** body between the thorax and pelvis," with an editor note observing that "In arthropods 'abdomen' is the most distal section of the body which lies behind the thorax or cephalothorax" (verified via [OLS4](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0000916)). This kills the whole GOLD `Abdomen` branch under `Arthropoda: Insects`, not just this leaf. |
| **UBERON:0000945** *stomach* / **BTO:0001307** *stomach* | The Latin false friend, and the grounding this record already retracted under #62. A vertebrate organ. |
| **HAO:0000369** *gaster* — "The anatomical cluster that is composed of all abdominal segments posterior to abdominal segment 2" | **An exact anatomical match, but out of scope for grounding.** HAO (Hymenoptera Anatomy Ontology) is not one of HabitatMech's five source vocabularies and is not in the vendored slice. It is also an *anatomy* term, not an environment term. Correct disposition: `relation: xref`. |
| **SIBO:0000113** *gaster* (Social Insect Behavior Ontology) | Same status as HAO — exact label match, out of scope, xref at most. Carries no definition in OLS. |

**Note on the repo's own rule.** CLAUDE.md's line — *"A host's PARTS ground to the anatomy term; the WHOLE host organism does not"* — puts the gaster firmly on the "parts" side, alongside gut, skin, lung and blood. It is a body region, not a taxon and not a life stage. The rule would ordinarily say "ground it." It cannot be applied here only because the anatomy term that exists (HAO:0000369) lives outside the five source ontologies. That is a vocabulary-coverage gap, not a conceptual one, and it is worth recording as such on the decision so a future slice expansion (cf. #10) picks it up.

---

## 3. Differentia — what distinguishes it

Ordered by how observable they are.

**(a) Host clade restriction.** The gaster is defined only for Apocrita — ants, bees and stinging/parasitoid wasps ([HAO:0000626 *metasoma*](https://www.ebi.ac.uk/ols4/ontologies/hao/classes?obo_id=HAO:0000626); [Gibson, Read & Fairchild 1998 chalcid glossary, cited as HAO's definition source](http://api.hymao.org/public/ontology_class/show_expanded/472)). A sibling "insect abdomen" habitat for a beetle or a fly is a different concept, because those insects have no petiole and no propodeal fusion.

**(b) Anatomical boundary at the wasp waist.** All abdominal segments posterior to A2 (or A3 where a postpetiole is present). This is the sharpest and most reliably observable differentia: a dissector separates the gaster at the waist, and the separation is mechanical and unambiguous.

**(c) It is an operational sampling unit, not just an anatomical region.** This is the differentia that makes it a *habitat* term rather than an anatomy term, and it is well documented:

- The Moreau lab's [*Ant Microbe Protocols*](https://cpb-us-e1.wpmucdn.com/blogs.cornell.edu/dist/0/8622/files/2013/08/Ant-Microbe-Protocols-Moreau.pdf) draws the line explicitly: gut dissection is required to claim you are studying *gut* microbes, whereas **whole gasters suffice when the target is ant-associated microbes more broadly**.
- [Chandler/Sanders et al. 2016, BMC Microbiology, doi:10.1186/s12866-016-0721-8](https://link.springer.com/article/10.1186/s12866-016-0721-8) pooled 3–5 **surface-sterilized whole gasters** per sample and validated the sterilization protocol against an alternative, precisely because cuticular DNA is inside the sampling boundary unless removed.
- [Lukasik/Kautz et al. 2021, Appl Environ Microbiol 87:e02803-20, doi:10.1128/AEM.02803-20](https://journals.asm.org/doi/10.1128/aem.02803-20) (published 26 Mar 2021) compared dissected crop, midgut, ileum and rectum against **entire gasters** across 492 samples and 11 *Cephalotes* species, concluding that "gaster samples can serve as a rough proxy for the microbial community found within the digestive tract" while being unable to resolve compartmentalization.

**(d) Internal compartmentalization with distinct communities.** Within one gaster the communities differ sharply by compartment: the *Cephalotes* midgut is dominated by Opitutales (genus *Cephaloticoccus*) at ~84% of the community, whereas ileum and rectum are led by Burkholderiales (26.3% and 25.7% respectively) alongside Xanthomonadales, Opitutales and Rhizobiales ([AEM 2021, doi:10.1128/AEM.02803-20](https://journals.asm.org/doi/10.1128/aem.02803-20)). A gaster sample is therefore a *mixture* by construction — a definitional property, not a caveat.

**(e) Characteristic physicochemistry: an actively acidified crop.** Formicine ants swallow their own formic-acid poison gland secretion via acidopore grooming, bending the gaster forward so the acidopore at its tip meets the mouth, and thereby maintain a strongly acidic crop lumen pH; this acts as a microbial filter that selectively permits Acetobacteraceae ([Tragust et al. 2020, eLife 9:e60287, doi:10.7554/eLife.60287, published 3 Nov 2020](https://elifesciences.org/articles/60287); [PMID 33138912](https://pubmed.ncbi.nlm.nih.gov/33138912/)). Note that this pH is a property of the gaster's *anterior* contents and of formicines specifically — do not generalize it to the gaster as a whole or to all Apocrita.

**(f) Intracellular niches, not only luminal ones.** The gaster is the only body region hosting the obligate endosymbiont niches: *Blochmannia* in midgut bacteriocytes intercalated between enterocytes, residing directly in the cytoplasm without a symbiosomal membrane, and invading oocytes for vertical transmission ([Stoll et al. 2010, doi:10.1186/1471-2180-10-308](https://bmcmicrobiol.biomedcentral.com/articles/10.1186/1471-2180-10-308); [Sauer et al. 2002](https://pubmed.ncbi.nlm.nih.gov/12200266/)); and *Wolbachia*, estimated at ~22% of ant species in one broad screen and infecting queen ovarioles and germline ([Russell et al. 2013, Psyche 2013:936341](https://www.hindawi.com/journals/psyche/2013/936341/); [Frost et al., JEB 223:jeb220079](https://journals.biologists.com/jeb/article/223/9/jeb220079/223800/Wolbachia-infected-ant-colonies-have-increased)). A whole-gaster extract therefore mixes luminal, intracellular and cuticular populations.

**(g) Social-transmission context.** The crop is the colony's shared food store, moved between individuals by oral trophallaxis and gated by the proventriculus ([AntWiki, Trophallaxis](https://www.antwiki.org/wiki/Trophallaxis)). Unlike a solitary insect gut, this gastral compartment is continuous across colony members — which is the mechanistic reason colony membership outweighs caste in structuring abdominal communities ([Segers et al. 2019, on *Temnothorax nylanderi*, PMC6912891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6912891/)).

---

## 4. Sources

Verified in this session (each fetched or returned by search above):

| Claim | Source |
|---|---|
| HAO definition of gaster; HAO:0000369 | [OLS4 / HAO](https://www.ebi.ac.uk/ols4/ontologies/hao/classes?obo_id=HAO:0000369); [Yoder et al. 2010, PLoS ONE 5:e15991, doi:10.1371/journal.pone.0015991](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0015991) |
| HAO metasoma definition and its Gibson/Read/Fairchild source | [HAO portal, metasoma](http://api.hymao.org/public/ontology_class/show_expanded/472) |
| Segment boundaries, petiole/postpetiole, tergite counts | [AntWiki, Morphological Terms/Worker Metasoma](https://www.antwiki.org/wiki/Morphological_Terms/Worker_Metasoma); [Wikipedia, Gaster (insect anatomy)](https://en.wikipedia.org/wiki/Gaster_(insect_anatomy)) |
| UBERON:0000916 is vertebrate-restricted | [OLS4 / UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0000916) |
| "gaster" as a related synonym of *stomach* | [OLS4 exact-synonym search](https://www.ebi.ac.uk/ols4/api/search?q=gaster&exact=true) |
| ENVO:01001002 definition and its three children | [OLS4 / ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002) |
| ENVO:01001033 *digestive tract environment*; ENVO:01001187 holothurian precedent | [OLS4 / ENVO search](https://www.ebi.ac.uk/ols4/api/search?q=digestive+tract+environment&ontology=envo) |
| Whole-gaster vs. dissected-compartment sampling; taxon dominance by compartment | [Appl Environ Microbiol 87:e02803-20, doi:10.1128/AEM.02803-20](https://journals.asm.org/doi/10.1128/aem.02803-20); [PMC8091110](https://pmc.ncbi.nlm.nih.gov/articles/PMC8091110/); [PMID 33579688](https://pubmed.ncbi.nlm.nih.gov/33579688/) |
| Pooled surface-sterilized whole gasters as a protocol | [BMC Microbiol, doi:10.1186/s12866-016-0721-8](https://link.springer.com/article/10.1186/s12866-016-0721-8) |
| "Dissect if you claim gut; whole gaster if you claim ant-associated" | [Moreau lab, *Ant Microbe Protocols*](https://cpb-us-e1.wpmucdn.com/blogs.cornell.edu/dist/0/8622/files/2013/08/Ant-Microbe-Protocols-Moreau.pdf) |
| Crop acidification by swallowed formic acid; acidopore at gaster tip | [eLife 9:e60287, doi:10.7554/eLife.60287](https://elifesciences.org/articles/60287); [PMID 33138912](https://pubmed.ncbi.nlm.nih.gov/33138912/) |
| *Blochmannia* in midgut bacteriocytes and oocytes | [BMC Microbiol 10:308, doi:10.1186/1471-2180-10-308](https://bmcmicrobiol.biomedcentral.com/articles/10.1186/1471-2180-10-308); [Sauer et al. 2002, AEM 68:4187–4193](https://pubmed.ncbi.nlm.nih.gov/12200266/) |
| *Wolbachia* prevalence and ovariole localization in ants | [Psyche 2013:936341](https://www.hindawi.com/journals/psyche/2013/936341/); [PMID 31334893](https://pubmed.ncbi.nlm.nih.gov/31334893/) |
| Colony > caste as the structuring factor for abdominal communities | [PMC6912891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6912891/) |
| Crop/proventriculus position within the gastral segments; trophallaxis | [AntWiki, Trophallaxis](https://www.antwiki.org/wiki/Trophallaxis); [digestive-anatomy figure after Eisner & Brown 1958](https://www.researchgate.net/figure/a-f-Digestive-anatomy-of-ants-a-Proventriculus-pv-in-the-context-of-the-digestive_fig1_8666351) |
| GOLD five-level ecosystem classification | [Mukherjee et al. 2023, Nucleic Acids Res, doi:10.1093/nar/gkac974](https://dx.doi.org/10.1093/nar/gkac974) |
| Low-biomass reagent-contamination caveat | flagged in the *Cephalotes* and insect-specimen-handling literature, e.g. [PMC4548535](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4548535/) |

**Cited from background knowledge, not verified in this session** — check before quoting in a note, since `tests/test_decisions.py` checks note claims: Lanan et al. 2016, "A bacterial filter protects and structures the gut microbiome of an insect," *ISME J* (proventriculus as a physical bacterial filter in *Cephalotes*); Sanders et al. 2014, *Mol Ecol*, "Stability and phylogenetic correlation in gut microbiota: lessons from ants and apes" ([PMID 24304129](https://pubmed.ncbi.nlm.nih.gov/24304129/) — record confirmed to exist, its whole-gaster methods not re-read here); Kwong & Moran 2016, *Nat Rev Microbiol* 14:374–384, ["Gut microbial communities of social bees"](https://www.nature.com/articles/nrmicro.2016.43) (record confirmed; used here only as background that the bee ileum/rectum communities sit in the same tagma).

**Explicitly my inference, not a source's statement:** (i) that GOLD's `Gaster` node denotes the sampling unit rather than the pure anatomical region — the path alone does not say so, though the sampling literature in §3(c) makes it the only workable reading; (ii) that the concept is Apocrita-restricted *as GOLD uses it* — GOLD's parent node is the far broader `Arthropoda: Insects`, so a submitter could in principle attach a non-hymenopteran sample to it.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**
- *gaster* (standard, Apocrita)
- *gastral segments* / *gastral region*
- *whole gaster* (the sampling-unit sense, as in the protocols above)
- loosely, *ant abdomen* / *abdomen* in microbiome papers that sample the whole region ([PMC6912891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6912891/) uses "abdomens" for what is anatomically the gaster) — a *usage*, not a term to import as an exact synonym

**Do not conflate**
- **stomach** (`UBERON:0000945`, `BTO:0001307`) — the Latin false friend; this was the retracted grounding.
- **abdomen** *sensu* general insect morphology — in Apocrita the true abdomen includes the propodeum (A1), which is fused into the mesosoma and lies outside the gaster.
- **metasoma** — the parent; includes petiole and postpetiole.
- **opisthosoma** — the chelicerate posterior tagma; a different clade's concept and a different HabitatMech branch.
- **gut / digestive tract / midgut / crop** — proper parts, each a legitimate distinct habitat; a whole-gaster sample is not a gut sample and the literature is explicit about the difference.
- **pedicel** — deprecated for the waist because it names the first funicular antennal segment elsewhere in Hymenoptera ([AntWiki](https://www.antwiki.org/wiki/Morphological_Terms/Worker_Metasoma)).
- **gaster flagging / gastral grooming** — behaviours, not places.

---

## 6. Should it be a term at all?

**Yes.** It is a physical body region that samples are literally taken from, with published protocols, a defined dissection boundary, and characterised microbial communities. It is not a process, quality, disease state, or taxon, and it is not a sampling artefact — if anything the reverse: the whole gaster is a *deliberate* sampling unit chosen over compartment dissection, so the concept has independent operational standing. `NOT_APPLICABLE` would be wrong.

**Recommended disposition** (matching the corpus's established patterns):

1. **Keep the minted identity** `habitatmech:GOLD.623ff8e506` and the `CONFIRM_UNGROUNDED` already recorded — the existing note is correct and the reasoning holds up.
2. **Add `HAO:0000369` (gaster) as `relation: xref`**, and optionally `SIBO:0000113`. Both are exact-label anatomical matches outside the five source vocabularies; an xref records the link without this repo asserting identity to a term it cannot validate against the vendored slice.
3. **Record the coverage gap explicitly**: this is not "no term exists in the world," it is "no term exists *in ENVO/UBERON/FOODON/BTO/PO*." Worth tagging for #10 (vendor-more-ontology) rather than leaving as an open definitional question.
4. **Two ENVO new-term requests are the real deliverable**, in this order of value:
   - `insect-associated environment` (or `arthropod-associated environment`) under ENVO:01001002 — this gap affects the entire `Arthropoda: Insects` branch, not just this leaf, and UBERON's vertebrate-only `abdomen` means the branch has no fallback either.
   - `gaster environment` under that, following the pattern ENVO already set with `holothurian digestive tract` (ENVO:01001187) — an existing precedent for a taxon-specific body-region environment class.
5. **Fix the parent first.** `Metasoma` (`habitatmech:GOLD.93f0f7b66d`) is `UNGROUNDED` from the class-level sweep with an explicit note that "whether the concept is a habitat at all was NOT assessed." It should be assessed the same way — it is the same kind of thing, one segment-pair broader, and `HAO:0000626` xrefs it exactly. Curating the child while the parent stays unassessed leaves the record's only `parent_habitats` link pointing at an undetermined concept.

**Priority: low.** `data/raw/gold_ecosystem_paths.tsv:1791` shows this path with all five assertion counters at zero — GOLD carries the vocabulary node but no organisms or biosamples are classified to it. It is a controlled-vocabulary leaf with no data behind it yet, so it sits at the bottom of the assertion-ranked backlog even though the concept itself is sound.

## Citations

1. https://www.ebi.ac.uk/ols4/ontologies/hao/classes?obo_id=HAO:0000369
2. https://www.antwiki.org/wiki/Morphological_Terms/Worker_Metasoma
3. https://www.researchgate.net/figure/a-f-Digestive-anatomy-of-ants-a-Proventriculus-pv-in-the-context-of-the-digestive_fig1_8666351
4. https://www.antwiki.org/wiki/Trophallaxis
5. https://pubmed.ncbi.nlm.nih.gov/12200266/
6. https://bmcmicrobiol.biomedcentral.com/articles/10.1186/1471-2180-10-308
7. https://www.wikidata.org/wiki/Q50422384
8. https://elifesciences.org/articles/60287
9. https://www.ebi.ac.uk/ols4/api/search?q=gaster&exact=true
10. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
11. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0000916
12. https://www.ebi.ac.uk/ols4/ontologies/hao/classes?obo_id=HAO:0000626
13. http://api.hymao.org/public/ontology_class/show_expanded/472
14. https://cpb-us-e1.wpmucdn.com/blogs.cornell.edu/dist/0/8622/files/2013/08/Ant-Microbe-Protocols-Moreau.pdf
15. https://link.springer.com/article/10.1186/s12866-016-0721-8
16. https://journals.asm.org/doi/10.1128/aem.02803-20
17. https://pubmed.ncbi.nlm.nih.gov/33138912/
18. https://www.hindawi.com/journals/psyche/2013/936341/
19. https://journals.biologists.com/jeb/article/223/9/jeb220079/223800/Wolbachia-infected-ant-colonies-have-increased
20. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6912891/
21. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0015991
22. https://en.wikipedia.org/wiki/Gaster_(insect_anatomy
23. https://www.ebi.ac.uk/ols4/api/search?q=digestive+tract+environment&ontology=envo
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC8091110/
25. https://pubmed.ncbi.nlm.nih.gov/33579688/
26. https://pubmed.ncbi.nlm.nih.gov/31334893/
27. https://dx.doi.org/10.1093/nar/gkac974
28. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4548535/
29. https://pubmed.ncbi.nlm.nih.gov/24304129/
30. https://www.nature.com/articles/nrmicro.2016.43