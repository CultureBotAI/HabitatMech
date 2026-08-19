---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T05:23:16.982065'
end_time: '2026-08-18T05:31:38.090257'
duration_seconds: 501.11
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Accessory nidamental gland (ANG)
  habitat_identifier: habitatmech:GOLD.453b1756ab
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Mollusca > Reproductive system > Accessory
    nidamental gland (ANG)'
  assertions: '0'
  parent_terms: (none)
  xrefs: (none)
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Variant-match\
    \ review (#12): the variant route reaches UBERON:0002788 'anterior nuclear group',\
    \ a region of the THALAMUS, for a mollusc reproductive gland \u2014 a match with\
    \ nothing behind it. UBERON has no nidamental gland term. Path: Host-associated\
    \ > Mollusca > Reproductive system > Accessory nidamental gland (source concept\
    \ habitatmech:GOLD.453b1756ab)"
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
  num_turns: 33
  total_cost_usd: 2.6379934999999994
  session_id: 8ebc6360-08bb-4e19-8da2-db7d4c655124
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 17
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Accessory nidamental gland (ANG)
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.453b1756ab
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Mollusca > Reproductive system > Accessory nidamental gland (ANG)
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Variant-match review (#12): the variant route reaches UBERON:0002788 'anterior nuclear group', a region of the THALAMUS, for a mollusc reproductive gland — a match with nothing behind it. UBERON has no nidamental gland term. Path: Host-associated > Mollusca > Reproductive system > Accessory nidamental gland (source concept habitatmech:GOLD.453b1756ab)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Accessory nidamental gland (ANG)** as a microbial habitat, with citations.

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

# Accessory nidamental gland (ANG) — definition research

**Concept:** `habitatmech:GOLD.453b1756ab` · HOST_ASSOCIATED · UNGROUNDED
**Source path:** `Host-associated > Mollusca > Reproductive system > Accessory nidamental gland (ANG)`

---

## Proposed definition

> A reproductive gland which lies in the mantle cavity of a sexually mature female decapodiform cephalopod, consists of epithelium-lined tubules whose lumina hold a dense extracellular bacterial consortium acquired from seawater, and which discharges that consortium into the jelly coat deposited around the animal's eggs.

Genus term available in the vendored slice: **`UBERON:0003937` "reproductive gland"** (verified present in `data/raw/ontology_terms.tsv`).

---

## 1. What the concept denotes

The ANG is a **paired glandular organ of female squids and cuttlefishes**, sitting in the mantle cavity adjacent to the nidamental glands (Collins et al. 2012 place it "posterior to the light organ and in close proximity to the nidamental gland" in *Euprymna scolopes*; comparative morphology usually describes the ANGs as anterior/proximal to the nidamental glands — see §4 note on the conflict). Its internal architecture is the reason it is a habitat: the organ is a dense mass of **blind-ending, epithelium-lined tubules, each tubule lumen packed with bacteria** ([Bloodgood 1977, *Tissue Cell* 9:197–208, doi:10.1016/0040-8166(77)90016-7](https://doi.org/10.1016/0040-8166(77)90016-7), PMID 906013). Light-sheet imaging of whole organs shows the ANG is "a composite tissue of individual, non-intersecting tubules that each harbor their own bacterial population," bisected, with tubules converging on two posterior points where they "empty into a space where bacteria can mix with squid jelly to be deposited onto eggs" ([Kamp et al. 2025, *Appl Environ Microbiol* 91(5):e0216324, doi:10.1128/aem.02163-24](https://doi.org/10.1128/aem.02163-24), PMID 40231847).

**What a sample is.** A GOLD "Accessory nidamental gland (ANG)" sample is the dissected gland — host epithelium plus the tubule-lumen consortium. The bacteria are **extracellular**, in the tubule lumina, not intracellular endosymbionts (Bloodgood 1977; Kamp et al. 2025).

**Boundary — inside the concept:**
- the tubule lumina and their bacterial consortium (the microbial habitat proper)
- the tubule epithelium and organ stroma (the host tissue defining the space)
- both pigmented (orange/red) and unpigmented (white/yellow) tubules, which carry measurably different communities ([Chiu et al. 2025, *Anim Microbiome* 7:36, doi:10.1186/s42523-025-00402-2](https://doi.org/10.1186/s42523-025-00402-2), PMID 40221798; correction doi:10.1186/s42523-025-00481-1)

**Boundary — neighbouring concepts, outside:**
- the **main/primary nidamental gland**, which secretes the egg jelly but is not a symbiont-housing organ
- the **egg jelly coat / egg capsule**, the downstream habitat the ANG inoculates ([Kerwin et al. 2019, *mBio* 10(5):e02376-19, doi:10.1128/mBio.02376-19](https://doi.org/10.1128/mBio.02376-19), PMID 31662458)
- the **light organ**, a separate symbiotic organ of the same animal, which GOLD already carries as its own path (`Host-associated > Mollusca > Sensory organs > Light organ`, `habitatmech:GOLD.200051736e`)
- the mantle cavity / mantle fluid, also separate GOLD paths

**Ambiguity: none material.** The abbreviation "ANG" collides with unrelated anatomy (see §5), but the label spelled out plus the source path `Mollusca > Reproductive system` fixes the reading unambiguously. The only real narrowing question is whether the concept means the *organ* or the *consortium-bearing lumen*; GOLD's path is anatomical, and the corpus treats organ-shaped host-associated paths anatomically, so the organ reading is the one to take. *(That last sentence is my inference from corpus practice, not a source claim.)*

---

## 2. Genus — the broader kind

The smallest well-established kind is **an accessory (non-gonadal) gland of the female reproductive system**.

| Candidate | Verdict |
|---|---|
| **`UBERON:0003937` "reproductive gland"** — "Any of the organized aggregations of cells that function as secretory or excretory organs and are associated with reproduction." | **Best available genus.** True of the ANG, asserts nothing the sources don't, and **is present in the vendored slice**. Broader than needed (it also subsumes male glands and the pituitary), which is the correct direction for a `parent_habitats` entry. |
| `UBERON:0005398` "female reproductive gland" | Tighter and still correct — and notably it already has an invertebrate accessory-gland child, `UBERON:0008935` "gastropod albumen gland", so it is not gonad-restricted. **Not in the vendored slice** (`grep` returns 0), so unusable as-is without vendoring (#10). Worth recording as the preferred genus for a term request. |
| `CEPH:0000001` "accessory nidamental gland" | **An exact identity match, but not a grounding target.** The Cephalopod Ontology names the concept, defined by its tubule ultrastructure. CEPH is **`activity_status: inactive`** in the OBO Foundry registry and has **zero terms in the vendored slice**. Use as `relation: xref`, not as identity. |
| `UBERON:0008975` "oviduct shell gland" | Near-miss. Defined as "a gland in the posterior expansion of the oviduct that secretes the calcareous surroundings of the egg shell" — the amniote shell gland. Wrong clade, wrong secretion, and asserts calcification the ANG does not do. |
| `ENVO:01000162` "organ", with children `ENVO:01000163` photophore, `ENVO:01000165` trophosome, `ENVO:01000166` mycetome, `ENVO:01000164` root nodule | **The strongest ENVO precedent, and still a near-miss.** ENVO already models symbiont-housing organs as environmental classes — including the *photophore*, i.e. the ANG's own sibling organ in this squid. But there is no ANG member, and `mycetome` is not it: mycetome is gut-linked, beetle-specific, and yeast-hosting per its own ENVO definition. `ENVO:01000162` is in the vendored slice and is a legitimate (very coarse) genus if the curator prefers ENVO framing over UBERON. |
| `ENVO:01001176` "environment associated with an aquatic invertebrate" / `ENVO:01001055` | Both vendored, both true of the ANG, but they are *whole-host* environment classes, not organ classes — several levels too coarse and they lose the "part of a host" claim the path makes. |
| `UBERON:0000990` "reproductive system" | Already the grounding of the parent record `habitatmech:GOLD.fcc934bd13` (NARROW). Correct but one level too coarse for this record. |

**No term names this concept in ENVO, UBERON, FOODON, BTO or PO.** An OLS-wide search for "nidamental" returns exactly four classes: `CEPH:0000001` (accessory nidamental gland), `CEPH:0000007` (main nidamental gland), `CEPH:0000175` (nidamental gland), and `UBERON:0008975` (oviduct shell gland). The existing curator note's conclusion stands — with the correction that **CEPH does name it**, which the note did not record.

---

## 3. Differentia — what distinguishes it

Against sibling glands of the female reproductive system, and against the other symbiotic organs of the same animal:

1. **Houses a resident, multi-species bacterial consortium in its tubule lumina.** This is the defining feature and the reason it is in a habitat corpus at all. Consortium composition in *E. scolopes*: Alphaproteobacteria 72.55% (dominant genus *Phaeobacter*, Rhodobacterales/*Roseobacter* clade), Verrucomicrobia 16.73%, Bacteroidetes/Flavobacteria 10.34%, Gammaproteobacteria <1% ([Collins et al. 2012, *Appl Environ Microbiol* 78(12):4200–08, doi:10.1128/AEM.07437-11](https://doi.org/10.1128/AEM.07437-11), PMID 22504817). In *Sepioteuthis lessoniana*: Proteobacteria 59%, Bacteroidetes 25%, Actinobacteria 6.7%, Firmicutes 5.3% ([Yang et al. 2021, *Microbes Environ* 36:ME21030, doi:10.1264/jsme2.ME21030](https://doi.org/10.1264/jsme2.ME21030), PMC8674444).
2. **Spatially partitioned — one tubule, often one taxon.** Tubules are non-intersecting and some are dominated by a single bacterial genus while others hold mixed populations (Collins et al. 2012; Kamp et al. 2025). This is an observable, imaging-verifiable property no sibling gland has.
3. **Environmentally (horizontally) acquired each generation, not vertically inherited.** Shown in *Loligo opalescens*, where developing tubules are still open to the mantle cavity and external seawater ([Kaufman et al. 1998, *Biol Bull* 194(1):36–43, doi:10.2307/1542511](https://doi.org/10.2307/1542511)); confirmed in *E. scolopes* (Collins et al. 2012) and *S. lessoniana* (Yang et al. 2021).
4. **Organ development itself depends on environmental bacteria.** Squid reared with depleted environmental microbiota had ANGs "completely absent or stunted," independently of the light-organ symbiont — described by the authors as the first example of complete organ development requiring symbiotic bacteria in an animal host ([McAnulty et al. 2023, *mBio* 14(1):e02131-22, doi:10.1128/mbio.02131-22](https://doi.org/10.1128/mbio.02131-22), PMID 36656023).
5. **Defensive output: the consortium is exported to the eggs.** Antibiotic treatment reduced egg bacterial load ~98% and dropped hatch rate to 9% versus 58% in untreated clutches, with heavy *Fusarium keratoplasticum* fouling; 87.5% of ANG isolates inhibited the fungus (Kerwin et al. 2019).
6. **Bacterially derived pigmentation tracks host sexual maturation.** The gland shifts from white to mottled red as the host matures, the colour arising from the resident bacteria — cultured isolates lose the pigment (Bloodgood 1977). Region-specific: Hyphomicrobiaceae are unique to orange regions, Fodinicurvataceae and Flavobacteriaceae to white regions (Chiu et al. 2025).
7. **Female-only and maturity-linked.** Restricted to sexually mature females (Collins et al. 2012; Bloodgood 1977).
8. **Taxon-restricted within Cephalopoda.** Present in Idiosepiidae, Sepiolidae, Sepiidae, Spirulidae, Loliginidae and Chtenopterygidae; absent in nautiloids and octopodiforms ([Lindgren et al. 2012, *BMC Evol Biol* 12:129](https://pmc.ncbi.nlm.nih.gov/articles/PMC3733422/)). Microbiome surveys span 11 species in 4 decapodiform families ([Vijayan et al. 2024, *Appl Environ Microbiol* 90(3):e0099023, doi:10.1128/aem.00990-23](https://doi.org/10.1128/aem.00990-23), PMID 38315021).

**Properties deliberately NOT in the proposed definition** (real but not definitional, or not verified): specific dominant taxa (they vary by host family — Vijayan et al. 2024 found significant between-family differences, Mantel *r* = 0.7 for phylosymbiosis, with sepiolids sharing ~50% *Opitutae* and *Ruegeria*); antimicrobial-compound production; carotenoid chemistry of the pigment (widely repeated in secondary summaries — **I did not verify it against a primary source and it should not enter the definition**); and oxygen tension / redox of the tubule lumen (**no source I found states it**; a Jan 2026 Nyholm-lab bioRxiv metagenomics preprint may address symbiont metabolism, but I did not confirm its contents).

---

## 4. Sources

| Claim | Source |
|---|---|
| Tubule ultrastructure; lumen packed with bacteria; white→mottled red on maturation; pigment is bacterial and lost in culture | Bloodgood RA 1977, *Tissue Cell* 9(2):197–208, [doi:10.1016/0040-8166(77)90016-7](https://doi.org/10.1016/0040-8166(77)90016-7), PMID 906013 |
| Horizontal colonization; tubules open to mantle cavity during development (*Loligo opalescens*) | Kaufman MR, Ikeda Y, Patton C, van Dykhuizen G, Epel D 1998, *Biol Bull* 194(1):36–43, [doi:10.2307/1542511](https://doi.org/10.2307/1542511) |
| Community composition and percentages; tubule partitioning; deposition into egg jelly coat; position posterior to light organ | Collins AJ et al. 2012, *Appl Environ Microbiol* 78(12):4200–08, [doi:10.1128/AEM.07437-11](https://doi.org/10.1128/AEM.07437-11), PMID 22504817, PMC3370523 |
| Roseobacter-clade isolate genomics (*Leisingera*, *Ruegeria*, *Tateyamaria*) | Collins AJ, Fullmer MS, Gogarten JP, Nyholm SV 2015, *Front Microbiol* 6:123, [PMC4337385](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4337385/) |
| Egg defence against fungal fouling; hatch-rate and antifungal statistics | Kerwin AH et al. 2019, *mBio* 10(5):e02376-19, [doi:10.1128/mBio.02376-19](https://doi.org/10.1128/mBio.02376-19), PMID 31662458 |
| Developmental timeline; epithelial field ~4 weeks post-hatch, pore proliferation | Kerwin AH, McAnulty SJ, Nyholm SV 2021, *Biol Bull* 240(3), [doi:10.1086/713965](https://doi.org/10.1086/713965) |
| Maturation-stage community shift; horizontal transfer (*S. lessoniana*) | Yang S-H et al. 2021, *Microbes Environ* 36:ME21030, [doi:10.1264/jsme2.ME21030](https://doi.org/10.1264/jsme2.ME21030) |
| ANG development requires environmental bacteria | McAnulty SJ, Kerwin AH et al. 2023, *mBio* 14(1):e02131-22, [doi:10.1128/mbio.02131-22](https://doi.org/10.1128/mbio.02131-22), PMID 36656023 |
| Cross-species microbiome survey; 11 species / 4 families / 7 locations; phylosymbiosis | Vijayan N et al. 2024, *Appl Environ Microbiol* 90(3):e0099023, [doi:10.1128/aem.00990-23](https://doi.org/10.1128/aem.00990-23), PMID 38315021 |
| Pigmented-region microbiomes; Hyphomicrobiaceae/orange, Flavobacteriaceae/white | Chiu L et al. 2025, *Anim Microbiome* 7:36, [doi:10.1186/s42523-025-00402-2](https://doi.org/10.1186/s42523-025-00402-2), PMID 40221798 |
| Whole-organ 3-D architecture; non-intersecting tubules; two posterior convergence points into the jelly | Kamp DL, Kerwin AH, McAnulty SJ, Nyholm SV 2025, *Appl Environ Microbiol* 91(5):e0216324, [doi:10.1128/aem.02163-24](https://doi.org/10.1128/aem.02163-24), PMID 40231847 |
| ANG vs light organ as two distinct symbiotic niches; shared immune gene families | Vijayan N, Briseño J, Simakov O, Nyholm SV 2026, *PNAS* 123(1):e2512903122, [doi:10.1073/pnas.2512903122](https://doi.org/10.1073/pnas.2512903122), PMID 41428895 |
| Phylogenetic distribution of the ANG across cephalopod families; absent in nautiloids and octopodiforms | Lindgren AR, Pankey MS, Hochberg FG, Oakley TH 2012, *BMC Evol Biol* 12:129, [PMC3733422](https://pmc.ncbi.nlm.nih.gov/articles/PMC3733422/) |
| `CEPH:0000001`, `CEPH:0000175`, `UBERON:0003937`, `UBERON:0005398`, `ENVO:01000162`+children | OLS4 API, queried 2026-08-18: [CEPH:0000001](https://www.ebi.ac.uk/ols4/ontologies/ceph/classes?obo_id=CEPH:0000001), [UBERON:0003937](https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0003937), [ENVO:01000162](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000162) |
| CEPH `activity_status: inactive` | [OBO Foundry registry](https://obofoundry.org/registry/ontologies.jsonld), retrieved 2026-08-18 |

**Conflict to flag for the curator.** Collins et al. 2012 writes that the ANG is found among "cephalopod mollusks (squid, octopuses, cuttlefish)"; Lindgren et al. 2012's morphological character matrix says female nautiloids and octopodiforms **lack** it. The comparative-morphology source is the better authority for a distribution claim, and the more recent microbiome survey (Vijayan et al. 2024) sampled only Decapodiformes. The proposed definition therefore says *decapodiform*. **Positional wording is likewise inconsistent across sources** (Collins: ANG posterior to the light organ, close to the nidamental gland; comparative sources: ANGs anterior to the nidamental glands) — this is why the proposed sentence says only "in the mantle cavity" and does not commit to an axis.

---

## 5. Synonyms, and what not to conflate

**Names in real use:** *accessory nidamental gland*; *ANG* (near-universal in the literature); *accessory nidamental glands* (the organ is paired); *accessory gland* (Bloodgood 1977's usage within a nidamental-gland context); *symbiotic reproductive organ* / *female symbiotic reproductive organ* (descriptive, used in titles — Vijayan et al. 2024, Kerwin et al. 2019).

**Do NOT conflate with:**

- **Nidamental gland / main nidamental gland** (`CEPH:0000175`, `CEPH:0000007`) — the jelly-secreting gland the ANG is accessory *to*. Distinct organ, not a symbiont-housing consortium habitat. This is the single most likely mis-grounding.
- **Light organ / photophore** (`ENVO:01000163`) — the other symbiotic organ of the same squid, a binary *Vibrio fischeri* association in extracellular crypts, and a **separate GOLD path already in this corpus** (`habitatmech:GOLD.200051736e`). Vijayan et al. 2026 treats the two as distinct niches with distinct communities.
- **Egg jelly coat / egg capsule** — the downstream habitat the ANG inoculates; a different sample and a different community context (Kerwin et al. 2019).
- **Oviducal gland** — a separate accessory gland of the cephalopod female tract.
- **`UBERON:0008975` "oviduct shell gland"** — amniote calcareous shell gland; lexically adjacent, biologically unrelated.
- **`UBERON:0002788` "anterior nuclear group"** — the thalamic region reached by the "ANG" abbreviation. Already recorded on this record's decision; worth carrying into the term-request note so a later automated pass does not rediscover it.
- **Mycetome / bacteriome** (`ENVO:01000166`) — ENVO's mycetome is gut-linked, beetle-specific and yeast-hosting; the ANG consortium is extracellular, bacterial, and reproductive-tract. Sibling under `ENVO:01000162` "organ", not a parent.
- **The whole squid, or Mollusca as a taxon** — per the repo's standing rule, the ANG is a host *part* and takes the anatomy term; the clade term does not.

---

## 6. Should it be a term at all — yes

The ANG is a physical, bounded, dissectible **place** inside a host, with an epithelium-defined lumen, a resident microbial community characterized in at least 11 host species across four families, and a demonstrated ecological function for those microbes. It is none of the dispositions that would argue against a term: not a process, not a quality, not a disease state, not a taxonomic grouping, not a sampling artefact. It is exactly the case CLAUDE.md's "a host's PARTS ground to the anatomy term" rule is written for — it fails to ground only because no term exists in the five vendored ontologies, which is the term-request condition, not the `NOT_APPLICABLE` condition.

**Suggested disposition:**

1. Keep `grounding_status: UNGROUNDED`; add **`UBERON:0003937` "reproductive gland"** to `parent_habitats` (vendored, verified label). This clears the `needs_a_parent_first.tsv` blocker, which currently reads "no ontology parent on the record, so there is no genus to write a definition from" — this report supplies both.
2. Add **`CEPH:0000001` "accessory nidamental gland"** with `relation: xref`. It is an exact identity match, but CEPH is OBO-inactive and unvendored, so it must not be used as an identity grounding.
3. Raise a term request. **UBERON is the better home than ENVO**: it already carries `UBERON:0005398` "female reproductive gland" with a molluscan accessory-gland child (`UBERON:0008935` gastropod albumen gland), giving a clean, precedented parent. Requesting an ENVO class instead is defensible and would fit the corpus's environment framing — `ENVO:01000162` "organ" already holds photophore, trophosome, mycetome and root nodule, i.e. ENVO's existing family of symbiont-housing organs, and the ANG's own sibling organ is already in it. A curator could reasonably request both: the anatomy term in UBERON and an `accessory nidamental gland environment` in ENVO.
4. Note for prioritization: upstream assertion volume is **0**, so this record buys no attestations. The literature depth is nonetheless unusually good for a novel term, and the ENVO/UBERON requests would be well-evidenced — but by `just report`'s ranking this is not high-yield backlog.

## Citations

1. https://doi.org/10.1016/0040-8166(77
2. https://doi.org/10.1128/aem.02163-24
3. https://doi.org/10.1186/s42523-025-00402-2
4. https://doi.org/10.1128/mBio.02376-19
5. https://doi.org/10.1128/AEM.07437-11
6. https://doi.org/10.1264/jsme2.ME21030
7. https://doi.org/10.2307/1542511
8. https://doi.org/10.1128/mbio.02131-22
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC3733422/
10. https://doi.org/10.1128/aem.00990-23
11. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4337385/
12. https://doi.org/10.1086/713965
13. https://doi.org/10.1073/pnas.2512903122
14. https://www.ebi.ac.uk/ols4/ontologies/ceph/classes?obo_id=CEPH:0000001
15. https://www.ebi.ac.uk/ols4/ontologies/uberon/classes?obo_id=UBERON:0003937
16. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01000162
17. https://obofoundry.org/registry/ontologies.jsonld