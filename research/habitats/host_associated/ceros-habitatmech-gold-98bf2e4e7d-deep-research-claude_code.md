---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T04:41:26.409531'
end_time: '2026-08-18T04:50:51.394714'
duration_seconds: 564.99
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Ceros
  habitat_identifier: habitatmech:GOLD.98bf2e4e7d
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Mammals > Integumentary system > Ceros'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Variant-match
    review (#12): the variant route reaches FOODON:03413986 ''cero'', which is a mackerel.
    The path is Mammals > Integumentary system, so this is a keratinous integumentary
    structure, not a fish. No term in the slice fits. Path: Host-associated > Mammals
    > Integumentary system > Ceros (source concept habitatmech:GOLD.98bf2e4e7d)'
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
  web_search_requests: 18
  num_turns: 37
  total_cost_usd: 3.7329289999999995
  session_id: b1365d30-b09b-4e44-b7c3-8ed140d25f38
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 20
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Ceros
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.98bf2e4e7d
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Mammals > Integumentary system > Ceros
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Variant-match review (#12): the variant route reaches FOODON:03413986 'cero', which is a mackerel. The path is Mammals > Integumentary system, so this is a keratinous integumentary structure, not a fish. No term in the slice fits. Path: Host-associated > Mammals > Integumentary system > Ceros (source concept habitatmech:GOLD.98bf2e4e7d)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Ceros** as a microbial habitat, with citations.

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

I'll research this concept now.

# Ceros — HabitatMech novel-term research

**Concept:** `habitatmech:GOLD.98bf2e4e7d` · label **Ceros** · HOST_ASSOCIATED · UNGROUNDED
**Sole attestation:** GOLD `Host-associated > Mammals > Integumentary system > Ceros` (`gold.ecosystem:6732`, `gold.ecosystem:6733`), **0 upstream assertions**

---

## Proposed definition

> A keratinous cranial appendage of a mammal, considered as the keratin-rich integumentary surface from which a microbial sample is taken.

**This sentence is deliberately weaker than the curator's usual target, and I recommend against minting it.** See §6: "Ceros" has no attested English referent, no sample ever classified under it, and the two readings that fit the evidence resolve either to a term the corpus already has (`UBERON:0006967` *horn*) or to a structure no ontology in the slice names (rhinoceros horn). Recording a fuller definition would mean choosing between those two by fiat.

---

## 1. What the concept denotes

**"Ceros" is not an anatomical term in English-language usage.** It is a Latinised transliteration of Greek κέρας / *keras* ("horn"), the second element of *rhinoceros* (ῥίς *rhis*, nose + κέρας, horn) and the root of *keratin*, *cerato-*, *Ceratotherium*, *Diceros*, *Triceratops* ([Etymonline, *kerato-*](https://www.etymonline.com/word/kerato-)). Checked against the standard anatomical literature, it appears as a bound morpheme, never as a free-standing structure name: neither Wikipedia's [*Horn (anatomy)*](https://en.wikipedia.org/wiki/Horn_(anatomy)) nor the [New World Encyclopedia entry](https://www.newworldencyclopedia.org/entry/Horn_(anatomy)) nor the comparative-anatomy reviews cited below uses "ceros" or "cerus" as a term. UBERON, ENVO, BTO, FOODON and PO contain no term with that label.

So the referent has to be inferred from GOLD's own vocabulary. The strongest evidence is the position of the node in GOLD's ecosystem CV. Under `Host-associated > Mammals > Integumentary system`, the node identifiers fall in a contiguous, evidently single-sitting block:

| GOLD node | Subtype |
|---|---|
| 6724 / 6725 | Claws |
| 6726 / 6727 | **Horn** |
| 6728 / 6729 | **Antlers** |
| 6730 / 6731 | **Pronghorn** |
| **6732 / 6733** | **Ceros** |
| 6734 / 6735 | Nails |
| 6736 / 6737 | Scales |

(from `data/raw/gold_ecosystem_paths.tsv`; GOLD's five-level scheme and its curation-driven, sample-led growth are described in [Ivanova et al. 2010, *Environ Microbiol* 12:1803–1805, doi:10.1111/j.1462-2920.2010.02216.x](https://doi.org/10.1111/j.1462-2920.2010.02216.x) and on the [GOLD Ecosystem Classification page](https://gold.jgi.doe.gov/ecosystem_classification))

That block is an enumeration of mammalian **keratinous integumentary appendages**, and its middle four entries are the canonical enumeration of mammalian headgear types in the order the comparative literature gives them — bovid horn, cervid antler, antilocaprid pronghorn, and then one more. The four extant pecoran headgear types are horns (Bovidae), antlers (Cervidae), pronghorns (Antilocapridae) and ossicones (Giraffidae) ([Davis, Brakora & Lee 2011, *Proc R Soc B* 278:2857–2865, doi:10.1098/rspb.2011.0938](https://doi.org/10.1098/rspb.2011.0938); [Wang et al. 2024, *Commun Biol* 7:632, doi:10.1038/s42003-024-06134-4](https://doi.org/10.1038/s42003-024-06134-4)). The fifth mammalian horn type, outside Ruminantia, is the rhinoceros horn ([Wikipedia, *Horn (anatomy)*](https://en.wikipedia.org/wiki/Horn_(anatomy))).

Grepping GOLD's whole CV: `ceros`, `antler`, `pronghorn`, `horn` return exactly four paths, all in this block. **GOLD has no node for "ossicone" and none for "rhinoceros horn" anywhere.**

### The two readings

**Reading A — rhinoceros horn (my best inference, not stated by any source).** GOLD's curator, enumerating mammalian headgear, wrote the Greek horn-word as a label for the rhinocerotid type, the one type otherwise absent from the list, and one whose ordinary English name ("rhinoceros horn") would collide confusingly with the sibling "Horn" two slots earlier. Under this reading the concept denotes the nasal or frontal horn of a rhinoceros (Rhinocerotidae): a solid, continuously growing epidermal structure of keratinised tubules dispersed in a keratin matrix, **not attached to and not containing a bony core** ([Ryder 1962, *Nature* 193:1199–1201, doi:10.1038/1931199a0](https://doi.org/10.1038/1931199a0); [Hieronymus, Witmer & Ridgely 2006, *J Morphol* 267:1172–1176, doi:10.1002/jmor.10465](https://doi.org/10.1002/jmor.10465)). A sample would be a swab or shaving of the horn's external surface or of its keratin body.

**Reading B — a Greek-language duplicate of the sibling "Horn."** "Ceros" simply means "horn," and GOLD acquired a redundant CV entry. Under this reading the concept is identical to `gold.ecosystem:6726` "Horn", which HabitatMech already grounds EXACT to `UBERON:0006967`.

I cannot distinguish these from the public record. GOLD publishes no definitions for CV nodes, `gold.jgi.doe.gov` returns HTTP 403 to unauthenticated fetches, and the node has **zero** projects, organisms or samples attached, so there is no sample metadata to disambiguate it. **Anything beyond "a keratinous cranial appendage of a mammal" is a choice between A and B, not a finding.**

### Boundary

Inside, under either reading: the keratinous horn structure and its surface. Outside, and each already a distinct GOLD sibling and a distinct HabitatMech record: **Horn** (`UBERON:0006967`), **Antlers** (`BTO:0001684`), **Pronghorn** (`habitatmech:GOLD.1e5645d6c8`, also UNGROUNDED), **Hoof** (`UBERON:0008963`), **Claws**, **Nails** (`UBERON:0001705`), **Scales**, **Hair/Fur**, and the surrounding **Skin** (which for rhinos is where the only published rhinoceros-integument microbiome work actually sampled — see §3).

---

## 2. Genus — the broader kind

**Smallest well-established kind: a keratinous cranial appendage (mammalian headgear).** Two candidate genus terms exist and both are already in the vendored slice:

- **`UBERON:0006969` *cranial appendage*** — "An anatomical projection that is part of and protrudes from the head." This is already the ontology parent HabitatMech assigns to its `Horn` record, so using it here is consistent with the corpus. It is the safest genus: true under both readings.
- **`UBERON:0000021` *cutaneous appendage*** — "Anatomical projection that protrudes from the skin. Examples: hair, nail, feather, claw, hoof, horn, wattle, spur, beak, antler, bristle and some scales." Broader; correct but less informative.

### ENVO check and near-misses

ENVO was checked directly (OLS4 API, `ontology=envo`, queries *horn*, *keratin*, *integument*, *animal-associated*) and against the vendored slice. **ENVO has no horn, headgear, or keratinous-appendage environment term.** The relevant ENVO terms are:

| Term | Why it is a near-miss, not a match |
|---|---|
| `ENVO:2100004` *integumental system environment* | The genus one level up, and already the concept the parent GOLD node maps to. Correct but far too broad — it covers skin, hair, mammary gland, sebum and adipose tissue equally. ENVO supplies **no textual definition** for it (confirmed via OLS4), so it cannot itself anchor a differentia. |
| `ENVO:01001002` *animal-associated environment* | "An environmental system determined by an animal." Two levels too broad. |
| `UBERON:0006967` *horn* | "A pointed projection of the skin on the head of various animals, consisting of a covering of horn (keratin and other proteins) surrounding **a core of living bone**." Under reading A this is a **positive over-claim**: rhinoceros horn has no bony core (Ryder 1962; Hieronymus et al. 2006), so grounding here would assert anatomy the sources deny. Under reading B it is an exact match and the record should merge into the existing `horn` record. This is the single decisive fork. |
| `UBERON:0006968` *keratin sheath of horn* | Narrower — the sheath alone, not the appendage. **Not in the vendored slice.** |
| `UBERON:0013213` *ossicone* | Not in the slice, and asserts a skin-and-fur-covered ossified-cartilage core with no keratin sheath — the opposite composition ([*Ossicone*, Wikipedia](https://en.wikipedia.org/wiki/Ossicone); Davis et al. 2011). |
| `UBERON:0009564` *distal limb integumentary appendage* | "A nail, hoof or claw" — right material, wrong body region. |
| `UBERON:0006971` *antler* | Not in the slice; shed bone, no keratin sheath; already the sibling concept. |
| `FOODON:03413986` *cero* | A mackerel (*Scomberomorus regalis*). Reached only by the variant-match route; already rejected in the recorded decision. |

**No term in the slice is a match.** The existing `CONFIRM_UNGROUNDED` is correct.

---

## 3. Differentia — what would distinguish it

Under **reading A** (rhinoceros horn), the observable properties that separate it from every sibling under *cranial appendage*:

- **Composition — entirely keratinous, no bony core.** Keratinised tubules ~300–500 µm across, each of ~40 layers of flattened dead cells, embedded in an amorphous matrix of keratinised spindle cells; a fibre-in-matrix composite (Ryder 1962; Hieronymus et al. 2006; [Van Orden & Daniel 1992, *MRS Proc* 292:45, doi:10.1557/PROC-292-45](https://doi.org/10.1557/PROC-292-45)). This distinguishes it from bovid *horn* (keratin sheath **over** living bone), *antler* (bare bone, no sheath), *pronghorn* (deciduous keratin sheath over a permanent bony blade), and *ossicone* (ossified cartilage under living skin and fur) — Davis et al. 2011; Wang et al. 2024.
- **Mineral and pigment gradient.** CT and histology show periodic banding attributable to melanin and to calcium phosphate salts (hydroxyapatite / octacalcium phosphate) concentrated in the core, which hardens the centre and lets the periphery wear back to a point (Hieronymus et al. 2006, doi:10.1002/jmor.10465).
- **Growth mode.** Continuous, unshed, pulsed growth from epidermal cells at the base over a dermal papilla, on the order of 5–6 cm yr⁻¹ in African species; not annually shed, unlike antler and pronghorn sheath (Ryder 1962; [Boy et al. 2015, *J Zool* 297:11–17, doi:10.1111/jzo.12229](https://doi.org/10.1111/jzo.12229)).
- **Anatomical position.** Median, on the nasal and/or frontal midline, not paired and lateral as in bovid horns and cervid antlers (Hieronymus et al. 2006).

**As a microbial habitat, the differentia is thin, and I found no primary study of it.** What is documented:

- **No horn-surface microbiome study exists for rhinoceros.** The only published survey of rhinoceros integument, [Zhong et al. 2023, *Microbiol Spectr* 11(4):e00921-23, doi:10.1128/spectrum.00921-23](https://doi.org/10.1128/spectrum.00921-23), sampled gut (faeces), **skin swabs**, and mud-bath soil from 15 captive white rhinos — explicitly not horn. It found skin and environmental communities converging on *Actinobacteriota*, *Chloroflexi* and *Proteobacteria* while gut was *Firmicutes*/*Bacteroidota*-dominated, with 22 phyla and 186 genera shared across niches — i.e. the rhinoceros body surface is largely soil-derived. That is a **skin** finding; extending it to horn is my inference.
- **Horn keratin is a real, characterised microbial substrate, but the literature is on detached/decaying horn, not living horn on a host.** *Onygena equina* (Onygenaceae) fruits specifically on putrefying horns of cattle and sheep and on hooves, and degrades their keratin — described as a "horn-destroying fungus" as early as [Ward 1899, *Proc R Soc Lond* 65:158, doi:10.1098/rspl.1899.0016](https://royalsocietypublishing.org/doi/10.1098/rspl.1899.0016), with mechanism work on the congener *O. corvina* in [*Appl Environ Microbiol* 2025, doi:10.1128/aem.01727-25](https://journals.asm.org/doi/10.1128/aem.01727-25). Bacterial keratinolysis of horn material is likewise documented: *Bacillus subtilis* MTCC 9102 was isolated from hornmeal (steam-processed horn and hoof) and extensively degrades it ([Balaji et al. 2008, *World J Microbiol Biotechnol* 24:2741–2745, doi:10.1007/s11274-008-9782-7](https://doi.org/10.1007/s11274-008-9782-7)); the general enzymology is reviewed in [Qiu et al. 2020, *Biotechnol Adv* 44:107607, doi:10.1016/j.biotechadv.2020.107607](https://doi.org/10.1016/j.biotechadv.2020.107607).

**A defensible microbial-habitat differentia would therefore be: a dry, nutrient-poor, hard α-keratin surface exposed to the ambient environment, colonisable chiefly by keratinolytic bacteria and fungi and by soil-derived taxa deposited from contact with substrate.** The keratinolysis half is well cited; the "soil-derived, resembling skin" half is **my inference from Zhong et al.'s skin data**, not something any source states about horn.

---

## 4. Sources

Every claim above is anchored to one of these; inferences are marked in-line.

| # | Source | Used for |
|---|---|---|
| 1 | Ivanova N et al. 2010. *Environ Microbiol* 12:1803–1805. [doi:10.1111/j.1462-2920.2010.02216.x](https://doi.org/10.1111/j.1462-2920.2010.02216.x); [GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification) | GOLD's five-level scheme; CV is curation- and sample-driven, so unused nodes can persist |
| 2 | [Etymonline, *kerato-*](https://www.etymonline.com/word/kerato-) | κέρας/*ceros* = horn; bound morpheme in *rhinoceros*, *keratin* |
| 3 | [Wikipedia, *Horn (anatomy)*](https://en.wikipedia.org/wiki/Horn_(anatomy)) (verified by direct fetch) | Enumeration of horn-like structures; rhino horn is keratin without bone core; **"ceros"/"cerus" absent from the article** |
| 4 | Davis EB, Brakora KA, Lee AH. 2011. *Proc R Soc B* 278:2857–2865. [doi:10.1098/rspb.2011.0938](https://doi.org/10.1098/rspb.2011.0938) | Four extant pecoran headgear types and their compositional differences |
| 5 | Wang Y et al. 2024. *Commun Biol* 7:632. [doi:10.1038/s42003-024-06134-4](https://doi.org/10.1038/s42003-024-06134-4) | Headgear definitions; homology of horn and antler |
| 6 | Ryder ML. 1962. *Nature* 193:1199–1201. [doi:10.1038/1931199a0](https://doi.org/10.1038/1931199a0) | Rhino horn is keratinised tubules in a keratin matrix — **not** agglutinated hair, and not bone-cored |
| 7 | Hieronymus TL, Witmer LM, Ridgely RC. 2006. *J Morphol* 267:1172–1176. [doi:10.1002/jmor.10465](https://doi.org/10.1002/jmor.10465); PMID 16823809 | CT/histology; melanin and calcium-phosphate banding; growth and external form |
| 8 | Boy SC et al. 2015. *J Zool* 297:11–17. [doi:10.1111/jzo.12229](https://doi.org/10.1111/jzo.12229) | White rhino horn development and structure |
| 9 | Van Orden A, Daniel JR. 1992. *MRS Proc* 292:45. [doi:10.1557/PROC-292-45](https://doi.org/10.1557/PROC-292-45) | Structure and composition of rhinoceros horn |
| 10 | Zhong L et al. 2023. *Microbiol Spectr* 11(4):e00921-23. [doi:10.1128/spectrum.00921-23](https://doi.org/10.1128/spectrum.00921-23) | White rhinoceros skin vs gut vs environment microbiota; **horn not sampled** |
| 11 | Ward HM. 1899. *Proc R Soc Lond* 65:158. [doi:10.1098/rspl.1899.0016](https://royalsocietypublishing.org/doi/10.1098/rspl.1899.0016); [*Onygena equina*, Wikipedia](https://en.wikipedia.org/wiki/Onygena_equina) | *O. equina* as an obligate horn/hoof keratin decomposer |
| 12 | Huang Y et al. 2025. *Appl Environ Microbiol*. [doi:10.1128/aem.01727-25](https://journals.asm.org/doi/10.1128/aem.01727-25) | Proteolytic and non-proteolytic keratin degradation in *Onygena corvina* |
| 13 | Balaji S et al. 2008. *World J Microbiol Biotechnol* 24:2741–2745. [doi:10.1007/s11274-008-9782-7](https://doi.org/10.1007/s11274-008-9782-7) | *Bacillus subtilis* MTCC 9102 isolated from and degrading hornmeal |
| 14 | Qiu J et al. 2020. *Biotechnol Adv* 44:107607. [doi:10.1016/j.biotechadv.2020.107607](https://doi.org/10.1016/j.biotechadv.2020.107607) | Bacterial and fungal keratinases; *Bacillus*, *Streptomyces*, *Nocardiopsis*, dermatophytes |
| 15 | Buttigieg PL et al. 2016. *J Biomed Semantics* 7:57. [doi:10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6) | ENVO scope for habitat representation |
| 16 | UBERON via OLS4 (`ebi.ac.uk/ols4/api`), queried 2026-08-18, plus `data/raw/ontology_terms.tsv` | Term labels, definitions and slice membership for `UBERON:0006967`, `:0006968`, `:0006969`, `:0000021`, `:0013213`, `:0009564`, `ENVO:2100004`, `ENVO:01001002` |

**Marked as inference, not sourced:** (a) that GOLD's "Ceros" denotes rhinoceros horn; (b) that rhinoceros horn surfaces carry soil-derived communities resembling rhinoceros skin; (c) that the ordering of GOLD nodes 6726→6732 reflects a single curator enumerating headgear types.

---

## 5. Synonyms, and what not to conflate

**Names in real use for the reading-A concept:** rhinoceros horn; rhino horn; nasal horn / anterior horn and frontal horn / posterior horn (positional, Hieronymus et al. 2006); *cornu* in older veterinary Latin. CITES trade documents and the forensic literature use "rhinoceros horn" exclusively — "ceros" appears in none of them.

**"Ceros" itself is in no real anatomical use** and should not be published as a synonym of anything without qualification.

**Do not conflate with:**

- **`UBERON:0006967` *horn*** (bovid true horn) — differs by the living bony core; the corpus already has this as the sibling `Horn` record. Under reading B they are the same and under reading A they are not, which is exactly why identity must not be asserted.
- **Antler** (`UBERON:0006971`, `BTO:0001684`) — shed bone, no keratin sheath.
- **Pronghorn** — deciduous keratin sheath over a permanent bony blade; already `habitatmech:GOLD.1e5645d6c8`, also UNGROUNDED.
- **Ossicone** (`UBERON:0013213`) — skin- and fur-covered ossified cartilage; giraffids only.
- **Cutaneous horn / *cornu cutaneum*** — a keratotic skin lesion in humans, a **clinical diagnosis**, not an appendage ([*Cutaneous horn*, Wikipedia](https://en.wikipedia.org/wiki/Cutaneous_horn)). A `NOT_APPLICABLE`-class concept if it ever surfaces.
- **`FOODON:03413986` *cero*** — the mackerel *Scomberomorus regalis*; a pure string collision, already rejected.
- **Uterine horn (`BTO:0004235`), anterior horn (spinal, `BTO:0005151`)** — unrelated senses of "horn" that lexical matching will reach.
- ***Ceras*/*cerata*** — dorsal outgrowths of nudibranchs; the same Greek root, a different phylum.
- ***Diceros*, *Ceratotherium*, *Monoceros*, *Oryctes rhinoceros*** — genus names containing the root; the last is a beetle whose gut microbiome is well studied and will pollute any literature search.

---

## 6. Should this be a term at all?

**No — I recommend leaving it as `CONFIRM_UNGROUNDED` with no term request, and adding `UBERON:0006967` only as `relation: xref`.**

The reasoning, in the corpus's own terms:

1. **It is not a not-a-habitat case.** "Ceros" is not a disease, quality, process, procedure, or taxon, so `NOT_APPLICABLE` would be the wrong and stronger claim. Whatever it denotes, it denotes a keratinous body structure, which is a legitimate place a microbe lives — and it is a *part*, not a whole organism, so the `#114`/`#112` host-vs-part rule points toward normal grounding, not toward an `<X>-associated environment` request.

2. **But it is very likely a source-vocabulary artefact.** The label is not in real anatomical use anywhere I could find; the node has never classified a single project, organism or sample (assertion volume 0, both node ids); and it sits two slots from a sibling, "Horn", that means exactly what the Greek word means. A CV that grows sample-by-sample (Ivanova et al. 2010) accumulates exactly this kind of unused, unexercised entry.

3. **The two surviving readings have opposite dispositions, and no evidence separates them.** Reading B says `GROUND` to `UBERON:0006967` *horn*. Reading A says that grounding is a positive over-claim, because `UBERON:0006967`'s definition asserts "a core of living bone" that rhinoceros horn does not have (Ryder 1962; Hieronymus et al. 2006) — the same shape of error as `#99`, where a term asserted an origin the source concept never claimed. Minting a term commits the corpus to reading A; grounding commits it to reading B. **`relation: xref` records the link GOLD's placement implies without asserting either.**

4. **A minted term here would be an unverifiable definition.** Under reading A there is genuinely no ontology term — UBERON has *horn*, *keratin sheath of horn*, *antler* and *ossicone* but nothing for rhinoceros horn, and ENVO has nothing in this space at all — so the gap is real. But nothing published says GOLD meant rhinoceros horn, and no study has ever sampled microorganisms from a rhinoceros horn. A definition written now would be sourced to my adjacency argument alone, which is exactly the plausible-sounding unverifiable claim `tests/test_decisions.py` exists to catch.

**If a curator wants to close this rather than leave it open,** the one action that would settle it is asking GOLD directly what node 6732 was created for — GOLD publishes no CV definitions and `gold.jgi.doe.gov` refuses unauthenticated requests, so it cannot be resolved from the public record. Until then, `CONFIRM_UNGROUNDED` plus an xref plus a note recording *both* readings is the honest state, and it is what the record already carries — the existing note's conclusion ("a keratinous integumentary structure, not a fish") is correct as far as it goes and could usefully be extended with the sibling-adjacency evidence and the bony-core objection above.

## Citations

1. https://www.etymonline.com/word/kerato-
2. https://en.wikipedia.org/wiki/Horn_(anatomy
3. https://www.newworldencyclopedia.org/entry/Horn_(anatomy
4. https://doi.org/10.1111/j.1462-2920.2010.02216.x
5. https://gold.jgi.doe.gov/ecosystem_classification
6. https://doi.org/10.1098/rspb.2011.0938
7. https://doi.org/10.1038/s42003-024-06134-4
8. https://doi.org/10.1038/1931199a0
9. https://doi.org/10.1002/jmor.10465
10. https://en.wikipedia.org/wiki/Ossicone
11. https://doi.org/10.1557/PROC-292-45
12. https://doi.org/10.1111/jzo.12229
13. https://doi.org/10.1128/spectrum.00921-23
14. https://royalsocietypublishing.org/doi/10.1098/rspl.1899.0016
15. https://journals.asm.org/doi/10.1128/aem.01727-25
16. https://doi.org/10.1007/s11274-008-9782-7
17. https://doi.org/10.1016/j.biotechadv.2020.107607
18. https://en.wikipedia.org/wiki/Onygena_equina
19. https://doi.org/10.1186/s13326-016-0097-6
20. https://en.wikipedia.org/wiki/Cutaneous_horn