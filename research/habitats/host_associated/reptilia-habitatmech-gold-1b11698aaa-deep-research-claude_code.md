---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:15:09.492404'
end_time: '2026-08-17T20:21:42.545223'
duration_seconds: 393.05
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Reptilia
  habitat_identifier: habitatmech:GOLD.1b11698aaa
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Reptilia'
  assertions: '133'
  parent_terms: ENVO:01001000
  xrefs: (none)
  decision_note: "Reviewed and endorsed the seeder's own resolution. xref-only review\
    \ (#43): kg-microbe maps this to NCBITaxon:8504, which is OVER-NARROW \u2014 Lepidosauria\
    \ excludes turtles and crocodilians, which Reptilia includes. The record carries\
    \ no xref for it: this is a GOLD path and the mapping-table route did not apply,\
    \ so the concept stays UNGROUNDED and the only trace of the mapping is upstream.\
    \ Reported as kg-microbe#790. Path: Host-associated > Reptilia (source concept\
    \ habitatmech:GOLD.1b11698aaa)"
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
  num_turns: 29
  total_cost_usd: 2.841238
  session_id: 5083cf02-6193-4675-a42a-d3c9c0755654
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 20
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Reptilia
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.1b11698aaa
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Reptilia
- **Upstream assertion volume:** 133
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Reviewed and endorsed the seeder's own resolution. xref-only review (#43): kg-microbe maps this to NCBITaxon:8504, which is OVER-NARROW — Lepidosauria excludes turtles and crocodilians, which Reptilia includes. The record carries no xref for it: this is a GOLD path and the mapping-table route did not apply, so the concept stays UNGROUNDED and the only trace of the mapping is upstream. Reported as kg-microbe#790. Path: Host-associated > Reptilia (source concept habitatmech:GOLD.1b11698aaa)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Reptilia** as a microbial habitat, with citations.

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

## Proposed definition

> An **animal-associated environment** which is determined by a non-avian reptile — an ectothermic amniote of the Testudines, Squamata, Rhynchocephalia or Crocodylia — whose keratinised, scaled integument and cloaca-terminating digestive tract are colonised by microbial communities structured by the host's environmentally determined body temperature.

If that reads as too much for one sentence, the defensible minimum is: *An animal-associated environment which is determined by a non-avian reptile (Testudines, Squamata, Rhynchocephalia or Crocodylia).* Everything after the dash is differentia that a curator can move into a comment; the clade enumeration is the part that cannot be dropped, because it is what fixes the paraphyletic reading (§1).

---

## 1. What the concept denotes

**The place sampled.** `Host-associated > Reptilia` denotes the body of a living reptile considered as an environment for microorganisms — its integument, oral cavity, alimentary tract, respiratory tract and internal organs, together with the material (faeces, saliva, swabs, tissue) taken from them. It is the whole-host environment, not the taxon: GOLD's own child paths carry the anatomy (`… > Digestive system > Large intestine > Fecal`, `… > Integumentary system > Skin`, `… > Respiratory system > Lung`, `… > Nervous system > Brain`, `… > Urinary system > Kidney`), and those are separate HabitatMech concepts that ground to UBERON/BTO in the ordinary way. The parent record is what remains when no body site is specified — 133 of the 214 assertions under the `Reptilia` subtree sit on the bare path.

**The label is ambiguous, and the ambiguity is consequential.** "Reptilia" has two live readings:

- **(a) Traditional / paraphyletic** — the four extant orders Testudines (turtles), Squamata (lizards, snakes, amphisbaenians), Rhynchocephalia (tuatara) and Crocodylia, *excluding* birds. This is the sense used throughout the reptile-microbiome literature, which speaks of "non-avian reptiles" as ectothermic tetrapods contrasted with the better-studied mammals ([Microbiol Mol Biol Rev, 2025, doi:10.1128/mmbr.00128-25](https://journals.asm.org/doi/10.1128/mmbr.00128-25); [J Appl Microbiol 132:2558, 2022](https://academic.oup.com/jambio/article/132/4/2558/6988740), which organises the class into exactly those four orders).
- **(b) Phylogenetic / crown-clade** — the least-inclusive clade containing turtles, lizards and crocodilians, which necessarily **includes Aves**; this is the sense of Modesto & Anderson's PhyloCode-conformant definition ([Syst Biol 53:815–821, 2004, doi:10.1080/10635150490503026](https://academic.oup.com/sysbio/article-abstract/53/5/815/2842963), PMID 15545258), and it is why NCBI Taxonomy carries **Sauropsida** (taxid 8457) under Amniota with **no Reptilia node at all**, and nests Aves (8782) inside it ([NCBI Taxonomy Browser, taxid 8457](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=8457)).

**The source data settles it as (a).** GOLD's `Host-associated` ecosystem categories are a flat, mutually exclusive list in which `Reptilia` sits beside `Birds`, `Amphibia`, `Fish`, `Mammals` and `Mammals: Human` (`data/raw/gold_ecosystem_paths.tsv`; the classification scheme itself is described in [Mukherjee et al., *Nucleic Acids Res* 51:D957–D963, 2023, doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204), and browsable at <https://gold.jgi.doe.gov/ecosystem_classification>). A sample classified `Host-associated > Birds` is by construction not `Host-associated > Reptilia`. **This is inference from the vocabulary's structure, not a statement GOLD makes in prose** — but it is the same inference any submitter makes when choosing between the two categories, and the definition should record it explicitly so the exclusion of birds is asserted rather than assumed.

**Boundaries.**

| Inside | Outside — and where it belongs |
|---|---|
| Any body site of a live turtle, tortoise, lizard, snake, amphisbaenian, tuatara or crocodilian | **Birds** — GOLD's sister category, `habitatmech:GOLD.47e603cf4f` |
| Faeces, saliva, cloacal swabs, skin swabs, sloughed skin from such a host | **Amphibia** — the other ectothermic tetrapod category, `NCBITaxon:8292` |
| Captive and wild hosts alike (GOLD does not distinguish) | **Reptile cage** — `Engineered > Built environment > Animal cage > Reptile cage`, a built environment, not a host |
| | **Eggshell and nest** — microbially real and well studied (see §3), but a maternally seeded external substrate, not host tissue; ENVO has `ENVO:02000004` *nesting material* |

---

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal"; synonyms *animal environment*, *Metazoan-associated environment*; EMPO alignment "Animal" ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)). A reptile is an animal, so the subsumption is unarguable and the differentia does the work.

This is also what the corpus already does for the sister clades: `birds.yaml`, `mammals.yaml` and `fish.yaml` all carry `ENVO:01001000` **and** `ENVO:01001002` as `parent_habitats`, and `habitatmech:GOLD.47e603cf4f` (Birds) was decided `CONFIRM_UNGROUNDED` against `ENVO:01001002` on the reasoning that grounding there would merge every host clade onto one record. **The Reptilia record currently carries only `ENVO:01001000`** — adding `ENVO:01001002` is a one-line consistency fix that the same decision row would make.

**Near-misses, and why each fails:**

| Candidate | Why it is not the answer |
|---|---|
| `ENVO:01001000` *environmental system determined by an organism* | Currently on the record. **Correct but too broad** — it does not assert animal-hood, which every source attestation does. Keep it (it is `ENVO:01001002`'s parent), but it is not the genus. |
| `ENVO:01001002` *animal-associated environment* | The genus, **not the identity**. Grounding here would collapse Reptilia, Birds, Mammals, Fish, Amphibia, Mollusca … onto one record. |
| A reptile-specific ENVO term | **Does not exist.** An OLS4 search of ENVO for "reptile" returns only `ENVO:02000004` *nesting material* (which merely mentions reptiles in its definition text) — no *reptile-associated environment*. The `<X>-associated environment` pattern is instantiated only at `ENVO:01001001` (plant), `ENVO:01001002` (animal), `ENVO:01001041` (fungi) and `ENVO:01001179` (cnidarian) in the vendored slice. This is the term-request gap. |
| `NCBITaxon:8504` *Lepidosauria* | kg-microbe's mapping, and **over-narrow** — Lepidosauria is lizards + snakes + tuatara only; it excludes Testudines and Crocodylia, both of which are inside the concept and both of which have published gut-microbiome data ([Hoffbeck et al. 2023](https://onlinelibrary.wiley.com/doi/10.1111/mec.17153)). Already recorded on the decision and reported as kg-microbe#790. It is the *only* candidate present in the vendored slice. |
| `NCBITaxon:8457` *Sauropsida* | **Over-broad and contradicts the source**: it includes Aves, which GOLD separates. Also **not in the vendored slice**. |
| `FOODON:03411625` *reptile* | Exists, but is a **taxon/food-source term with no textual definition** in FOODON, and is not in the vendored slice. The corpus has repeatedly reversed FOODON organism groundings of exactly this shape (`algae`, `mollusc`, `echinoderm`, `fungus`) under the organism-identity screen (#109). |
| `mesh:D012104` *Reptiles*, `SNOMED:107241004` *Class Reptilia* | Real terms in real vocabularies, and MeSH CURIEs are already used as xrefs elsewhere in `curation/decisions.tsv` (e.g. `mesh:D003063` Cnidaria). **Neither is in the vendored slice**, so neither can be cited today without vendoring (#10). Both are taxon terms in any case, so at best `relation: xref`. |

**Net finding: no term in ENVO, UBERON, FOODON, BTO or PO names this habitat, and no taxon term in the vendored slice covers traditional Reptilia.** The existing note's conclusion — UNGROUNDED, no xref recorded — is correct on the present slice, and the reason is now stronger than "the mapping table route did not apply": *there is nothing correct to point at.*

---

## 3. Differentia — what distinguishes it from its siblings

Each of these separates the concept from `Birds`, `Mammals` and `Amphibia` under the same genus.

**a. Ectothermy — the host has no fixed body temperature, and the microbiome tracks it.** This is the single strongest differentia against Birds and Mammals, and it is experimentally supported rather than merely anatomical. Warming altered and destabilised the gut microbiota of fence lizards, with composition associated with host thermal tolerance ([Moeller et al., *Appl Environ Microbiol* 86:e01181-20, doi:10.1128/aem.01181-20](https://journals.asm.org/doi/10.1128/aem.01181-20)); manipulating the microbiota reciprocally reduced host thermal tolerance and fitness under heat stress ([*Nat Ecol Evol*, 2022, doi:10.1038/s41559-022-01686-2](https://www.nature.com/articles/s41559-022-01686-2)); long-term warming of *Eremias multiocellata* decreased gut diversity at 2 months but increased it at 13 and 27 months, with faecal transplants confirming a causal effect on immune capacity ([*Microbiome*, 2023, doi:10.1186/s40168-023-01736-2](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-023-01736-2)); thermal sensitivity itself differs between warm- and cold-climate lizards ([*Front Microbiol* 15:1374209, 2024](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1374209/full)). The MMBR review devotes a section to microbiome–temperature stress for exactly this reason ([doi:10.1128/mmbr.00128-25](https://journals.asm.org/doi/10.1128/mmbr.00128-25)).

**b. Keratinised, scaled, gland-poor integument shed periodically.** Reptile skin is a dry, keratinised, scale-bearing surface replaced wholesale by ecdysis rather than continuously desquamated — a materially different microbial surface from feathered, furred or mucous-covered (amphibian) integument. The reptile skin microbiome is explicitly identified as the least-studied compartment: despite dermatological disease being among the commonest reptile diseases, only a few studies report reptilian skin microbiota ([Skin microbiota altered in crocodile lizards with skin ulcer, *Front Microbiol*, PMC8884271](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8884271/); reviewed in [doi:10.1128/mmbr.00128-25](https://journals.asm.org/doi/10.1128/mmbr.00128-25)). *Caveat for the curator:* the "no sweat glands / gland-poor" claim is standard herpetological anatomy but I did not find it asserted in a microbiome-context source — cite a herpetology reference or drop it.

**c. A cloaca as the single terminal outlet.** Digestive, urinary and reproductive tracts converge on one chamber, which is why cloacal swabbing is the standard non-destructive sampling proxy for the reptile gut and why GOLD's faecal path (30 assertions, the largest single child) is what most samples actually are ([*Front Microbiol* 14:1263917, 2023](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1263917/full), which cleans the external cloaca with alcohol first to exclude environmental microbiota). Shared with birds, not with mammals or fish.

**d. Oviparity with little or no parental care, giving cloaca-mediated vertical transmission.** In *Sceloporus virgatus*, oviposited eggs — those that passed through the maternal cloaca — carried more bacteria and fewer fungal hyphae than dissected eggs, had different eggshell communities, higher hatch success and larger offspring ([Bunker et al., *Anim Microbiome* 3:43, 2021, doi:10.1186/s42523-021-00104-5](https://animalmicrobiome.biomedcentral.com/articles/10.1186/s42523-021-00104-5)). In *Mauremys reevesii*, eggshell communities resembled maternal cloaca, maternal skin and nest soil but not surrounding soil or pond water — mixed vertical/horizontal transmission without parental care ([*Front Microbiol* 13:911416, 2022, doi:10.3389/fmicb.2022.911416](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2022.911416/full)).

**e. A limited core microbiota and strong order-level structure.** A uniform re-analysis of 745 gut samples from 91 reptile species found significant alpha- and beta-diversity differences by host order, environment, diet, habitat and conservation status, with **diet and host order contributing most**, and recovered only a **limited core microbiota** across reptiles ([Hoffbeck et al., *Mol Ecol* 32:6044–6058, 2023, doi:10.1111/mec.17153](https://onlinelibrary.wiley.com/doi/10.1111/mec.17153)). No published gut data exist for the tuatara, the sole extant rhynchocephalian. This matters for the definition: *the concept is heterogeneous by construction*, which argues for a genus-differentia definition anchored on host biology rather than on community composition.

**f. Asymptomatic *Salmonella* carriage as a near-universal background.** *Salmonella* is regarded as part of the normal reptile gut community, carried asymptomatically and shed intermittently. In clinically healthy animals: snakes 56.0%, lizards 36.9%, tortoises 34.2%, turtles 18.6%, crocodilians 9%; captive animals shed significantly more than wild-sampled ones ([Pees et al., 2023, PMC10562597](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10562597/)). ARAV, with CDC, advises presuming every reptile and amphibian is carrying it, since intermittent shedding makes culture-negative results uninformative ([ARAV guidelines](https://arav.org/salmonella-in-reptiles-and-amphibians-veterinary-guidelines/)); roughly 6% of sporadic human salmonellosis is attributed to direct or indirect reptile contact ([CDC *Emerg Infect Dis* 31(10), 2025](https://wwwnc.cdc.gov/eid/article/31/10/24-1803_article)). **Do not put this in the definition** — it is a characteristic occupant, not a defining property of the place, and shared with amphibians. It belongs in a comment, and it is the historical reason reptile microbiology was culture-based and disease-focused for decades ([doi:10.1128/mmbr.00128-25](https://journals.asm.org/doi/10.1128/mmbr.00128-25)).

**Scale, for context:** the Reptile Database's 2023 release listed 11,940 living species plus 2,158 subspecies, the overwhelming majority squamates; the total moves by roughly 200 species a year ([reptile-database.org news](http://www.reptile-database.org/db-info/news.html)). Cite it as "approximately 12,000 living species" rather than a fixed number.

---

## 4. Sources

Primary literature and reviews
- Microbiome in reptile health, disease and ecology (review; skin, oral, gut, eggshell, nest, temperature stress). *Microbiol Mol Biol Rev*, 2025. doi:10.1128/mmbr.00128-25 — <https://journals.asm.org/doi/10.1128/mmbr.00128-25>
- Hoffbeck C, Middleton DMRL, Nelson NJ, Taylor MW. 16S rRNA gene-based meta-analysis of the reptile gut microbiota. *Mol Ecol* 32:6044–6058, 2023. doi:10.1111/mec.17153 — <https://onlinelibrary.wiley.com/doi/10.1111/mec.17153>
- Gut microbiome–immune system interaction in reptiles. *J Appl Microbiol* 132:2558, 2022 — <https://academic.oup.com/jambio/article/132/4/2558/6988740>
- Moeller AH et al. The lizard gut microbiome changes with temperature and is associated with heat tolerance. *Appl Environ Microbiol* 86:e01181-20, 2020. doi:10.1128/aem.01181-20 — <https://journals.asm.org/doi/10.1128/aem.01181-20>
- Experimental manipulation of microbiota reduces host thermal tolerance and fitness under heat stress in a vertebrate ectotherm. *Nat Ecol Evol*, 2022. doi:10.1038/s41559-022-01686-2 — <https://www.nature.com/articles/s41559-022-01686-2>
- Gut microbiota modulation enhances the immune capacity of lizards under climate warming. *Microbiome*, 2023. doi:10.1186/s40168-023-01736-2 — <https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-023-01736-2>
- Microbial communities are thermally more sensitive in warm-climate lizards. *Front Microbiol* 15:1374209, 2024 — <https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1374209/full>
- Responses of gut microbiota in crocodile lizards to temperature. *Front Microbiol* 14:1263917, 2023 — <https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1263917/full>
- Bunker ME et al. Vertically transmitted microbiome protects eggs from fungal infection and egg failure. *Anim Microbiome* 3:43, 2021. doi:10.1186/s42523-021-00104-5 — <https://animalmicrobiome.biomedcentral.com/articles/10.1186/s42523-021-00104-5>
- Mixed-mode bacterial transmission via eggshells in an oviparous reptile without parental care. *Front Microbiol* 13:911416, 2022. doi:10.3389/fmicb.2022.911416 — <https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2022.911416/full>
- Skin microbiota altered in crocodile lizards with skin ulcer. *Front Microbiol*, 2022 — <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8884271/>
- Pees M et al. *Salmonella* in reptiles: occurrence, interactions, shedding and risk factors, 2023 — <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10562597/>
- Reptile exposure in human salmonellosis cases, Ontario 2015–2022. *Emerg Infect Dis* 31(10), 2025 — <https://wwwnc.cdc.gov/eid/article/31/10/24-1803_article>

Nomenclature and vocabularies
- Modesto SP, Anderson JS. The phylogenetic definition of Reptilia. *Syst Biol* 53:815–821, 2004. doi:10.1080/10635150490503026, PMID 15545258 — <https://academic.oup.com/sysbio/article-abstract/53/5/815/2842963>
- NCBI Taxonomy, Sauropsida taxid 8457 (no Reptilia node; Aves 8782 nested within) — <https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=8457>
- Mukherjee S et al. Twenty-five years of GOLD: v.9. *Nucleic Acids Res* 51:D957–D963, 2023. doi:10.1093/nar/gkac974 — <https://academic.oup.com/nar/article/51/D1/D957/6786204>; ecosystem classification — <https://gold.jgi.doe.gov/ecosystem_classification>
- ENVO `ENVO:01001002` *animal-associated environment* — <https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002>
- ARAV/CDC *Salmonella* veterinary guidelines — <https://arav.org/salmonella-in-reptiles-and-amphibians-veterinary-guidelines/>
- The Reptile Database species statistics — <http://www.reptile-database.org/db-info/news.html>

**Explicitly my inference, not sourced:** (i) that GOLD's `Reptilia` excludes birds — supported by the mutually exclusive sibling categories in `data/raw/gold_ecosystem_paths.tsv`, not by GOLD prose; (ii) that `ENVO:01001002` is the right genus — a subsumption judgement; (iii) the "gland-poor integument" clause in §3b; (iv) the negative result that ENVO has no reptile-associated environment term — an OLS4 search on 2026-08-17, which a later ENVO release could falsify.

---

## 5. Synonyms, and what not to conflate

**Usable synonyms** (all for the traditional, non-avian reading)
- *reptile-associated environment* — the ENVO-pattern name, and the recommended primary label if a term is requested
- *non-avian reptile-associated environment* — unambiguous, and the phrasing the microbiome literature uses
- *reptile host* / *reptilian host*
- *Reptilia* (as GOLD writes it), *reptiles*
- *herptile* / *herpetofauna* — **only partially**; these conventionally bundle amphibians and are therefore broader (see below)

**Do not conflate**
- **Sauropsida / crown Reptilia** — includes birds; over-broad. GOLD's `Birds` is a separate category with 1,848 assertions of its own.
- **`NCBITaxon:8504` Lepidosauria** — over-narrow; excludes Testudines and Crocodylia. This is the recorded upstream error (kg-microbe#790).
- **Amphibia** (`NCBITaxon:8292`) — separate GOLD category; moist, gland-rich, mucus-covered skin, aquatic larval stages. "Herps" and "herpetofauna" cover both and must not be used as a synonym for either alone.
- **The taxon term itself** — `FOODON:03411625` *reptile*, `mesh:D012104` *Reptiles*, `SNOMED:107241004` *Class Reptilia* all denote a class of organisms, not a place. Per the repo's #114 rule these belong in `relation: xref`, never as identity or as `parent_habitats`.
- **`Engineered > Built environment > Animal cage > Reptile cage`** — a husbandry surface, not a host.
- **Reptile eggshell / nest substrate** — maternally seeded but external; a distinct concept (`ENVO:02000004` *nesting material* is the nearest existing term).
- **"Reptile" as food** — FOODON's framing of reptiles as a food commodity is a different concept from a host environment.

---

## 6. Should it be a term at all? — Yes

Under the repo's own rule (CLAUDE.md, #114): *an organism acting as a host **is** a habitat; the taxon term is not*. Reptilia here is a host clade with 133 direct assertions and 214 across its subtree, and ENVO already models precisely this pattern at plant-, animal-, fungi- and cnidarian-associated environment. `NOT_APPLICABLE` would be wrong — this is not a disease, quality, process or procedure, and `tests/test_decisions.py` would fail a `NOT_APPLICABLE` pointing at an organism term anyway.

**Recommended disposition — mirror the Birds row exactly:**

| Field | Value |
|---|---|
| key | `habitatmech:GOLD.1b11698aaa` |
| decision | `CONFIRM_UNGROUNDED` |
| target / label | `ENVO:01001002` / `animal-associated environment` (as parent, not identity — same as `habitatmech:GOLD.47e603cf4f`) |
| effect on record | adds `ENVO:01001002` to `parent_habitats` alongside the existing `ENVO:01001000`, matching `birds.yaml`, `mammals.yaml`, `fish.yaml` |

**On the xref.** The existing note is right that the record carries no xref, and the reason is now firmer: **no term covering traditional Reptilia exists in the vendored slice.** `NCBITaxon:8504` is the only reptile-ish term vendored and it is over-narrow; `NCBITaxon:8457` Sauropsida is over-broad *and* absent; `FOODON:03411625` and `mesh:D012104` are absent. Two honest options —

1. **Leave it xref-free** (status quo, and defensible): recording an over-narrow xref publishes a claim the sources do not make, the same over-claim pattern that #99 was about.
2. **Vendor `mesh:D012104` *Reptiles*** (MeSH CURIEs already appear in `decisions.tsv`) and attach it as `relation: xref`. This is the smallest slice extension that lets the record point at something that actually denotes the concept.

I recommend (1) for this pass and filing (2) as a slice-extension issue against #10, so that the choice is a reviewable one-line decision rather than a silent one.

**Term-request note.** The gap is a real one and it is clade-wide, not Reptilia-specific: ENVO instantiates `<X>-associated environment` for plants, animals, fungi and cnidarians, but not for any vertebrate class. Birds, Mammals, Fish, Amphibia and Reptilia are all sitting `CONFIRM_UNGROUNDED` against the same parent for the same reason. If a term request is ever raised, raising it once as a coordinated set of vertebrate-class `<X>-associated environment` terms is stronger than five separate requests — but per the standing rule, no submission goes out without explicit per-request approval.

## Citations

1. https://journals.asm.org/doi/10.1128/mmbr.00128-25
2. https://academic.oup.com/jambio/article/132/4/2558/6988740
3. https://academic.oup.com/sysbio/article-abstract/53/5/815/2842963
4. https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=8457
5. https://academic.oup.com/nar/article/51/D1/D957/6786204
6. https://gold.jgi.doe.gov/ecosystem_classification
7. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
8. https://onlinelibrary.wiley.com/doi/10.1111/mec.17153
9. https://journals.asm.org/doi/10.1128/aem.01181-20
10. https://www.nature.com/articles/s41559-022-01686-2
11. https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-023-01736-2
12. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1374209/full
13. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8884271/
14. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1263917/full
15. https://animalmicrobiome.biomedcentral.com/articles/10.1186/s42523-021-00104-5
16. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2022.911416/full
17. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10562597/
18. https://arav.org/salmonella-in-reptiles-and-amphibians-veterinary-guidelines/
19. https://wwwnc.cdc.gov/eid/article/31/10/24-1803_article
20. http://www.reptile-database.org/db-info/news.html