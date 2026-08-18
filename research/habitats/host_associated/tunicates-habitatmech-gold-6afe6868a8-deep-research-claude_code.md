---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-18T02:50:03.480636'
end_time: '2026-08-18T02:59:05.980357'
duration_seconds: 542.5
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Tunicates
  habitat_identifier: habitatmech:GOLD.6afe6868a8
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Invertebrates > Tunicates'
  assertions: '0'
  parent_terms: (none)
  xrefs: FOODON:03414466
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term FOODON:03414466 'tunicate' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.6afe6868a8)"
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
  web_search_requests: 16
  num_turns: 31
  total_cost_usd: 3.5275835
  session_id: 311e1323-57b8-48ad-aee9-16b3055d5039
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 30
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Tunicates
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.6afe6868a8
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Invertebrates > Tunicates
- **Upstream assertion volume:** 0
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** FOODON:03414466

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term FOODON:03414466 'tunicate' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.6afe6868a8)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Tunicates** as a microbial habitat, with citations.

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

# Tunicates as a microbial habitat — definition research

**Target:** `habitatmech:GOLD.6afe6868a8` · label "Tunicates" · HOST_ASSOCIATED · UNGROUNDED
**Source path:** GOLD `Host-associated > Invertebrates > Tunicates` (gold.ecosystem:8463/8464/8465) · 0 assertions

---

## Proposed definition

> An environment associated with an aquatic invertebrate which is determined by the body of a tunicate (Chordata: Tunicata) — its cellulosic tunic, branchial sac, gut or cloacal cavity — and which sustains a host-specific microbial community compositionally distinct from the seawater the animal continuously filters.

Genus taken verbatim from **ENVO:01001176** *environment associated with an aquatic invertebrate* (in the vendored slice; `rdfs:subClassOf` ENVO:01001002 *animal-associated environment* and ENVO:01001055).

---

## ⚠️ Read this before writing the definition: this concept is a duplicate

The corpus holds **two** minted GOLD concepts labelled "Tunicates", differing only in where GOLD hung them:

| Record | Identifier | GOLD path | Assertions | Children |
|---|---|---|---|---|
| `tunicates__07723248.yaml` | `habitatmech:GOLD.78c645fff9` | `Host-associated > Tunicates` | 23 ORGANISM | `> Ascidians` (79 ORGANISM) |
| **this one** — `tunicates.yaml` | `habitatmech:GOLD.6afe6868a8` | `Host-associated > Invertebrates > Tunicates` | **0** | none |

Both already carry the identical CONFIRM_UNGROUNDED note and the identical `FOODON:03414466` xref. `data/raw/gold_ecosystem_paths.tsv` confirms both paths and the zero count on this one.

Nothing in the source data distinguishes the two *denotations*. GOLD's ecosystem vocabulary is explicitly a finite, non-exhaustive, periodically-revised term list rather than a strict classification, and it accumulates alternate paths to the same concept as curators add samples ([Mukherjee et al. 2023, *Nucleic Acids Research* 51:D957–D963, doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204)). `Host-associated > Invertebrates > Tunicates` reads as a re-placement of the same host clade under the `Invertebrates` category, not a narrower or different kind of place — and it carries no genomes at all, which is what you would expect of a path added but never populated.

**Recommendation:** decide this one `SAME_AS habitatmech:GOLD.78c645fff9` rather than authoring a second definition for the same clade. `curation/decisions.tsv` already supports `SAME_AS` (one existing use), and it exists for exactly this (#116/#117). Everything below then supports the *single* surviving Tunicates definition. If the curator prefers to keep two records, the definitions must be word-identical, or the corpus publishes two different accounts of one clade.

Note one thing the definition must **not** do: assert that tunicates are non-chordates. GOLD's parent node says "Invertebrates", and that is defensible only because *Invertebrata* is a paraphyletic grade rather than a clade — tunicates are chordates and are the **sister group of vertebrates**, not an early-branching side-line ([Delsuc et al. 2006, *Nature* 439:965–968, doi:10.1038/nature04336](https://www.nature.com/articles/nature04336); [PubMed 16495997](https://pubmed.ncbi.nlm.nih.gov/16495997/)). ENVO:01001176's own definition says only "a metazoan which lacks a vertebral column", which is literally true of every tunicate, so the genus is safe; a differentia that says "invertebrate animal" in the taxonomic sense would not be.

---

## 1. What the concept denotes

**The living body of a tunicate, in all its compartments, as the place a microbial sample is taken from.**

Tunicata is a subphylum of ~3,000 described, **exclusively marine**, filter-feeding chordates ([Delsuc et al. 2018, *Mol. Phylogenet. Evol.* 124:166–176, doi:10.1016/j.ympev.2018.01.009](https://pubmed.ncbi.nlm.nih.gov/29330139/); [Braun, Leubner & Stach 2020, *Cladistics* 36:259–300, doi:10.1111/cla.12405](https://onlinelibrary.wiley.com/doi/full/10.1111/cla.12405)). Three conventional classes:

- **Ascidiacea** — sea squirts; sessile, benthic, solitary or colonial, 10 mm to 60 cm, colonies to metres
- **Thaliacea** — salps, doliolids, pyrosomes; holoplanktonic
- **Appendicularia (Larvacea)** — free-swimming, house-building, mostly millimetric

(The three-class scheme is contested — Thaliacea is nested within "Ascidiacea" in molecular trees, making Ascidiacea likely artificial — but that affects sub-terms, not this one. Same sources.)

**Inside the concept**, as sampled compartments, each documented as a distinct microbial habitat:

| Compartment | Evidence it is a distinct microbial habitat |
|---|---|
| **Tunic** (outer cellulosic test) | 42 GBR samples / 25 species, tunic-only sampling; 3,217 OTUs from 19 described + 14 candidate phyla ([Erwin et al. 2014, *ISME J* 8:575–588, doi:10.1038/ismej.2013.188](https://www.nature.com/articles/ismej2013188)) |
| **Branchial sac** | Distinct from tunic in the same animal: 72 OTUs differed significantly between amphipod and tunic, only 3 between amphipod and branchial sac ([Hutchings et al. 2024, *Environ. Microbiol. Rep.* 16:e13242, doi:10.1111/1758-2229.13242](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1758-2229.13242)) |
| **Gut / digestive tract** | *Ciona* gut carries a core microbiota across geographically disparate populations ([Dishaw et al. 2014, *PLoS ONE* 9:e93386, doi:10.1371/journal.pone.0093386](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0093386)); germ-free *Ciona* can be generated and re-colonised ([Leigh, Liberti & Dishaw 2016, *Front. Microbiol.* 7:2092, doi:10.3389/fmicb.2016.02092](https://pubmed.ncbi.nlm.nih.gov/28082961/)) |
| **Cloacal cavity** (colonial didemnids) | Effectively a monoculture of extracellular *Prochloron didemni* ([Kühl et al. 2012, *PLoS ONE* 7:e31567, PMC3510431](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510431/)) |
| **Intracellular / bacteriocyte-like** | *Ca.* Endoecteinascidia frumentensis inside host cells of *Ecteinascidia turbinata* ([Schofield et al. 2015, *Environ. Microbiol.* 17:3964–3975, doi:10.1111/1462-2920.12908](https://enviromicro-journals.onlinelibrary.wiley.com/doi/abs/10.1111/1462-2920.12908)); *Photobacterium* Pa-1 intracellular in pyrosome light organs ([Berger et al. 2021, *Front. Mar. Sci.* 8:606818, doi:10.3389/fmars.2021.606818](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2021.606818/full)) |
| **Surface biofilm of pelagic colonies** | 128 pyrosome-specific ASVs; Planctomycetes, Actinomycetes, predatory Myxococcales — "pyrosome colonies are living hosts to a complex surface-associated microbial community" ([Thompson et al. 2021, *ISME Communications* 1:11, doi:10.1038/s43705-021-00007-1](https://www.nature.com/articles/s43705-021-00007-1)) |

**Boundary — what is a neighbouring concept, not this one:**

- **`Ascidians`** (`habitatmech:GOLD.34c28836da`, GOLD `Host-associated > Tunicates > Ascidians`, 79 organisms) — a *child*: class Ascidiacea only, excluding thaliaceans and larvaceans. Also `BTO:0000090` *ascidian*, already an EXACT-grounded record in the corpus. The Tunicates term must stay broad enough to cover the two pelagic classes, or it collapses into Ascidians.
- **The seawater being filtered.** A tunicate is a high-throughput seawater pump; salp guts are full of ingested diatoms, dinoflagellates and haptophytes with rapid transit ([Kelly & Suthers 2017, *Mar. Biol.* 164:161, doi:10.1007/s00227-017-3174-1](https://link.springer.com/article/10.1007/s00227-017-3174-1)). Much of what a 16S survey recovers is transient prey. The boundary against `sea water` is drawn empirically by host-specificity, not anatomically — see §3.
- **Abandoned larvacean houses.** Discarded at up to one every 3–4 h and flux rates of 20,000–120,000 houses m⁻² d⁻¹, they become classic marine snow with their own colonising community ([Davoll & Silver 1986, *Mar. Ecol. Prog. Ser.* 33:111–120](https://www.int-res.com/abstracts/meps/v33/p111-120/)). **This is a genuine reading split and I am flagging it rather than deciding it:** while occupied the house is part of the animal's feeding apparatus; once abandoned it is detritus and belongs with marine snow / particulate organic matter, not here. Recommend the definition say "the body of a tunicate" and leave abandoned houses out.
- **Tunicate as food.** *Halocynthia roretzi* (sea pineapple, 멍게/ホヤ) is farmed and eaten. A *processed or fermented sea-squirt product* is a food habitat (FOOD category), not HOST_ASSOCIATED. Live farmed animals are still this concept.
- **The taxon Tunicata itself** (`NCBITaxon:7712`, in the slice) — a class of organisms, not a place. Stays `relation: xref` per #99.

**Is the label ambiguous?** Not in denotation — "Tunicates" unambiguously names the subphylum in every source consulted. The only ambiguity is the duplicate-path one in the box above, and the food/organism reading that `FOODON:03414466` invites.

---

## 2. Genus — the broader kind

**Recommended: `ENVO:01001176` *environment associated with an aquatic invertebrate*.**

Verified from the vendored slice (`data/raw/ontology_terms.tsv`) and OLS:

> "An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system." *(sic — "vetebral" is upstream's typo)*
> `rdfs:subClassOf` ENVO:01001002, ENVO:01001055 (`data/raw/ontology_subclass_edges.tsv`)

It is *broader* than the concept, which is what a genus should be, and — unlike the crustacean case — every one of its two conditions holds of the whole clade without exception: all ~3,000 tunicates are marine, and none has a vertebral column. This matters, because the corpus explicitly rejected this term for `Arthropoda: Crustaceans` on the ground that it "excludes terrestrial crustaceans" (`curation/decisions.tsv`, `habitatmech:GOLD.2959225799`). That objection does not transfer: there are no terrestrial or freshwater tunicates. **This concept can use a tighter genus than its crustacean sibling could, and the reason is a fact about the clade, not a change of policy.**

### Near-misses and why each fails

| Term | Label | Why it is not an identity match |
|---|---|---|
| `ENVO:01001002` | animal-associated environment | Broader — covers every metazoan host. The corpus convention parent for host clades (Invertebrates, Ascidians, Crustaceans all use it). **Safe fallback genus** if the curator wants consistency over precision; the cost is a definition whose genus discards "marine" and "invertebrate", both of which are true. |
| `ENVO:01001055` | environment associated with an animal part or small animal | Asserts *part* or *small animal*. Larvaceans are millimetric, but ascidian colonies span metres. Asserting "small" over the clade is an over-claim. |
| `ENVO:01001000` | environmental system determined by an organism | Far too broad (current parent on the sibling record `GOLD.78c645fff9`); would not distinguish a tunicate from a rhizosphere. |
| `FOODON:03414466` | tunicate | **Not an environment at all.** Its slice definition is a description of the *animals* ("Tunicates … are members of the Tunicata, a subphylum of the phylum Chordata. They are marine filter feeders…"). Grounding a habitat here would ground a place to an organism/food class — the exact error #99 and #114 record. Correct only as `relation: xref`, as it currently is. |
| `NCBITaxon:7712` | Tunicata | A taxon. Present in the slice — **arguably the cleaner xref target than FOODON**, since FOODON's term exists to name a food source and NCBITaxon's names the clade the GOLD path means. Suggest adding it alongside, or in place of, the FOODON xref. |
| `BTO:0000090` | ascidian | Narrower (Ascidiacea) and a biological-source term; already its own corpus record. |
| `UBERON:0009719` | tunicate siphon | In the slice, and genuinely tunicate anatomy — but a *part*, orders of magnitude narrower. Worth noting for a future sub-habitat: siphons are the documented portal of entry for *Azumiobodo hoyamushi* ([Kumagai et al. 2014, *J. Invertebr. Pathol.* 120:32–37](https://pubmed.ncbi.nlm.nih.gov/24991851/)), so "tunicate siphon" is a real sampled site. |
| `BTO:0003173` | endostyle | Same shape of near-miss: a tunicate/cephalochordate organ, not the animal. |

I searched the slice (13,611 terms) for `tunic`, `ascidia`, `sea squirt`, `salp`, `pyrosom`, `larvacea`, `urochord`; the table above is the complete set of hits relevant to this concept. **No ENVO term names a tunicate-associated environment.** ENVO has plant-, animal- and fungi-associated environment but no per-clade marine-invertebrate terms — there is no sponge-associated or coral-associated environment term either, which is why the corpus's Sponge, Porifera and Cnidaria records are all likewise term-request candidates. UNGROUNDED is the right status, and an ENVO term request (`tunicate-associated environment`) is the right disposition.

---

## 3. Differentia — what distinguishes it from its siblings

Four properties separate a tunicate-associated environment from the other aquatic-invertebrate hosts under the same genus. The first two are the strongest because they are physical and clade-universal.

**(a) A cellulosic body wall — unique among animals.** The tunic is an acellular extracellular coat secreted by the epidermis, whose defining constituent is cellulose ("tunicin"). Tunicates are the **only metazoans that synthesise cellulose**, via a cellulose synthase (*CesA*) acquired by horizontal transfer from an actinobacterium into the tunicate ancestor, fused with a GH6-family cellulase domain; ORTHOSCOPE recovers *CesA* in all eight sequenced tunicate genomes and in no other animal genome ([Sasakura et al. 2019, *Genes* 10:294, doi:10.3390/genes10040294](https://doi.org/10.3390/genes10040294); [Sagane et al. 2016, *Proc. R. Soc. B* 283:20161712, doi:10.1098/rspb.2016.1712](https://royalsocietypublishing.org/doi/10.1098/rspb.2016.1712)). This is exactly the kind of differentia a definition wants: the dominant material of the habitat surface is a β-glucan, not the chitin of an arthropod, the aragonite of a coral, the collagen-and-spicule mesohyl of a sponge, or the calcium-carbonate shell of a mollusc. Marine Actinobacteria are found in the ascidian digestive tract, which is the proposed transfer route (same sources).

**(b) A host-specific community sustained inside a continuous seawater filter.** This is the differentia that separates the habitat from the ambient sea it is bathed in, and it is measured, not assumed:

- 71% of the 3,217 tunic OTUs were rare and specific to a single host species; host phylogenetic relatedness correlated with symbiont community similarity; several rare seawater microbes were enriched **200–700-fold** in the tunic relative to seawater (Erwin et al. 2014, above).
- Pyrosome communities were significantly *less* diverse than seawater (Chao1 p = 0.02; Shannon p < 0.01) and dominated by two novel bacterial groups, one ASV reaching 92% of sequences in a single specimen (Thompson et al. 2021, above).
- The pattern holds in invasive and introduced species, where the ascidian microbiome separates cleanly from bacterioplankton into a stable core plus a dynamic fraction ([Casso et al. 2020, *Front. Mar. Sci.* 7:201, doi:10.3389/fmars.2020.00201](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2020.00201/full); [Evans et al. 2017, *Sci. Rep.* 7:11033, doi:10.1038/s41598-017-11441-4](https://www.nature.com/articles/s41598-017-11441-4)).

**(c) Signature symbionts not found in the sibling host clades.** Three are diagnostic and each is separately characterised:

- ***Prochloron didemni*** — a large (7–25 µm) chlorophyll-*b*-containing cyanobacterium, obligately symbiotic and never cultured, packed extracellularly in the cloacal cavities of (sub)tropical didemnid ascidians, supplying reduced carbon and nitrogen on nutrient-poor reefs and encoding the patellamide pathway *patA–patG*, confirmed by heterologous expression in *E. coli* ([Schmidt et al. 2005, *PNAS* 102:7315–7320, doi:10.1073/pnas.0501424102](https://www.pnas.org/doi/10.1073/pnas.0501424102); [Kühl et al. 2012, PMC3510431](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510431/)). The *Lissoclinum patella* metagenome shows the holobiont is far more than *Prochloron*: patellazole is not in the *Prochloron* genome and traces to another member ([Donia et al. 2011, *PNAS* 108:E1423–E1432, doi:10.1073/pnas.1111712108](https://www.pnas.org/content/108/51/E1423)).
- ***Ca.* Endoecteinascidia frumentensis** — a γ-proteobacterial obligate endosymbiont with a ~0.6 Mb reduced genome, assembled directly from *Ecteinascidia turbinata* metagenomic DNA, and the true producer of ET-743 (trabectedin / Yondelis®), the approved soft-tissue-sarcoma drug long attributed to the tunicate itself (Schofield et al. 2015, above; [U. Michigan news release, 27 May 2015](https://news.umich.edu/pinpointing-natural-cancer-drug-s-true-origins-brings-sustainable-production-a-step-closer/)).
- ***Photobacterium* Pa-1** — >50% of pyrosome bacterial taxa were bioluminescent Vibrionaceae; FISH localised Pa-1 around the periphery of each light organ, intracellularly, at 40–74% relative abundance (Berger et al. 2021, above). Note the open question: a RLuc-like luciferase in the pyrosome transcriptome suggests an endogenous route too ([Tessler et al. 2020, *Sci. Rep.* 10:17724, doi:10.1038/s41598-020-73446-w](https://www.nature.com/articles/s41598-020-73446-w)) — do not let the definition assert bacterial origin of pyrosome light.

Ammonia-oxidising Thaumarchaeota were found in 24 of 25 GBR host species (Erwin et al. 2014), and universal core OTUs in introduced ascidians map to nitrogen cycling, UV protection and heavy-metal processing (Evans et al. 2017) — a functional signature worth recording, though "the community performs nitrification" is a stronger claim than any single one of these papers makes for the clade.

**(d) The habitat exists in both benthic and holoplanktonic settings.** Unlike sponges or corals, tunicate-associated environments are not tied to a substrate: ascidians are sessile on hard bottom, thaliaceans and appendicularians spend their whole lives in the water column, and both carry host-specific communities (Erwin et al. 2014 vs. Thompson et al. 2021). **A definition must not say "benthic".**

---

## 4. Sources

Full citations for every claim above, in order of first use:

1. Mukherjee S, *et al.* (2023) Twenty-five years of Genomes OnLine Database (GOLD): data updates and new features in v.9. *Nucleic Acids Research* 51(D1):D957–D963. [doi:10.1093/nar/gkac974](https://academic.oup.com/nar/article/51/D1/D957/6786204) · PMID 36318257 · PMC9825498. (Correction: *NAR* 52(6):3483, 2024, doi:10.1093/nar/gkae162.)
2. Delsuc F, Brinkmann H, Chourrout D, Philippe H (2006) Tunicates and not cephalochordates are the closest living relatives of vertebrates. *Nature* 439:965–968. [doi:10.1038/nature04336](https://www.nature.com/articles/nature04336) · PMID 16495997 · [open text](https://hal.science/halsde-00315436/document).
3. Delsuc F, *et al.* (2018) A phylogenomic framework and timescale for comparative studies of tunicates / Phylogenomics offers resolution of major tunicate relationships. *Mol. Phylogenet. Evol.* 124:166–176. [PubMed 29330139](https://pubmed.ncbi.nlm.nih.gov/29330139/).
4. Braun K, Leubner F, Stach T (2020) Phylogenetic analysis of phenotypic characters of Tunicata supports basal Appendicularia and monophyletic Ascidiacea. *Cladistics* 36:259–300. [doi:10.1111/cla.12405](https://onlinelibrary.wiley.com/doi/full/10.1111/cla.12405).
5. Erwin PM, Pineda MC, Webster N, Turon X, López-Legentil S (2014) Down under the tunic: bacterial biodiversity hotspots and widespread ammonia-oxidizing archaea in coral reef ascidians. *ISME J* 8(3):575–588. [doi:10.1038/ismej.2013.188](https://www.nature.com/articles/ismej2013188) · PMID 24152714 · PMC3930322.
6. Hutchings JA, *et al.* (2024) Distinct microbial communities in an ascidian–crustacean symbiosis. *Environ. Microbiol. Rep.* 16:e13242. [doi:10.1111/1758-2229.13242](https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1758-2229.13242) · PMC10881349.
7. Dishaw LJ, *et al.* (2014) The gut of geographically disparate *Ciona intestinalis* harbors a core microbiota. *PLoS ONE* 9(4):e93386. [doi:10.1371/journal.pone.0093386](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0093386).
8. Leigh BA, Liberti A, Dishaw LJ (2016) Generation of germ-free *Ciona intestinalis* for studies of gut–microbe interactions. *Front. Microbiol.* 7:2092. [doi:10.3389/fmicb.2016.02092](https://pubmed.ncbi.nlm.nih.gov/28082961/).
9. Kühl M, *et al.* (2012) Microenvironmental ecology of the chlorophyll *b*-containing symbiotic cyanobacterium *Prochloron* in the didemnid ascidian *Lissoclinum patella*. *PLoS ONE* / *Front. Microbiol.* — [PMC3510431](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510431/).
10. Schmidt EW, Nelson JT, Rasko DA, Sudek S, Eisen JA, Haygood MG, Ravel J (2005) Patellamide A and C biosynthesis by a microcin-like pathway in *Prochloron didemni*, the cyanobacterial symbiont of *Lissoclinum patella*. *PNAS* 102(20):7315–7320. [doi:10.1073/pnas.0501424102](https://www.pnas.org/doi/10.1073/pnas.0501424102) · PMID 15883371.
11. Donia MS, Fricke WF, Ravel J, Schmidt EW (2011) Complex microbiome underlying secondary and primary metabolism in the tunicate–*Prochloron* symbiosis. *PNAS* 108(51):E1423–E1432. [doi:10.1073/pnas.1111712108](https://www.pnas.org/content/108/51/E1423) · PMC3251135.
12. Schofield MM, Jain S, Porat D, Dick GJ, Sherman DH (2015) Identification and analysis of the bacterial endosymbiont specialized for production of the chemotherapeutic natural product ET-743. *Environ. Microbiol.* 17(10):3964–3975. [doi:10.1111/1462-2920.12908](https://enviromicro-journals.onlinelibrary.wiley.com/doi/abs/10.1111/1462-2920.12908) · PMID 26013440 · [free manuscript, OSTI 1344906](https://www.osti.gov/pages/biblio/1344906).
13. Berger A, *et al.* (2021) Microscopic and genetic characterization of bacterial symbionts with bioluminescent potential in *Pyrosoma atlanticum*. *Front. Mar. Sci.* 8:606818. [doi:10.3389/fmars.2021.606818](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2021.606818/full).
14. Thompson AW, *et al.* (2021) Host-specific symbioses and the microbial prey of a pelagic tunicate (*Pyrosoma atlanticum*). *ISME Communications* 1:11. [doi:10.1038/s43705-021-00007-1](https://www.nature.com/articles/s43705-021-00007-1) · PMID 36721065 · PMC9723572. Published 14 Apr 2021.
15. Tessler M, *et al.* (2020) A putative chordate luciferase from a cosmopolitan tunicate indicates convergent bioluminescence evolution across phyla. *Sci. Rep.* 10:17724. [doi:10.1038/s41598-020-73446-w](https://www.nature.com/articles/s41598-020-73446-w).
16. Sasakura Y, *et al.* (2019) ORTHOSCOPE analysis reveals the presence of the cellulose synthase gene in all tunicate genomes but not in other animal genomes. *Genes* 10(4):294. [doi:10.3390/genes10040294](https://doi.org/10.3390/genes10040294).
17. Sagane Y, *et al.* (2016) Transcriptional regulation of a horizontally transferred gene from bacterium to chordate. *Proc. R. Soc. B* 283:20161712. [doi:10.1098/rspb.2016.1712](https://royalsocietypublishing.org/doi/10.1098/rspb.2016.1712) · PMC5204163.
18. (2024) Molecular control of cellulosic fin morphogenesis in ascidians. *BMC Biology* 22. [doi:10.1186/s12915-024-01872-7](https://link.springer.com/article/10.1186/s12915-024-01872-7).
19. Kelly P, Suthers IM, *et al.* (2017) Gut contents and isotopic profiles of *Salpa fusiformis* and *Thalia democratica*. *Mar. Biol.* 164:161. [doi:10.1007/s00227-017-3174-1](https://link.springer.com/article/10.1007/s00227-017-3174-1).
20. Davoll PJ, Silver MW (1986) Marine snow aggregates: life history sequence and microbial community of abandoned larvacean houses from Monterey Bay, California. *Mar. Ecol. Prog. Ser.* 33:111–120. [int-res.com](https://www.int-res.com/abstracts/meps/v33/p111-120/).
21. Casso M, Turon X, Pascual M (2020) The microbiome of the worldwide invasive ascidian *Didemnum vexillum*. *Front. Mar. Sci.* 7:201. [doi:10.3389/fmars.2020.00201](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2020.00201/full).
22. Evans JS, Erwin PM, Shenkar N, López-Legentil S (2017) Introduced ascidians harbor highly diverse and host-specific symbiotic microbial assemblages. *Sci. Rep.* 7:11033. [doi:10.1038/s41598-017-11441-4](https://www.nature.com/articles/s41598-017-11441-4) · PMC5591302.
23. Utermann C, *et al.* (2020) Culture-dependent microbiome of the *Ciona intestinalis* tunic: isolation, bioactivity profiling and untargeted metabolomics. *Microorganisms* 8(11):1732. [PMC7694362](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7694362/). (89 bacterial and 22 fungal strains; first fungal isolations from the *Ciona* tunic.)
24. Kumagai A, *et al.* (2014) *Azumiobodo hoyamushi*, the kinetoplastid causing soft tunic syndrome in ascidians, may invade through the siphon wall. *J. Invertebr. Pathol.* 120:32–37. [PubMed 24991851](https://pubmed.ncbi.nlm.nih.gov/24991851/).
25. Hirose E, *et al.* (2014) Quantitative assessment of *Azumiobodo hoyamushi* distribution in the tunic of soft tunic syndrome-affected ascidian *Halocynthia roretzi* using real-time PCR. *Parasites & Vectors* 7:539. [doi:10.1186/s13071-014-0539-x](https://link.springer.com/article/10.1186/s13071-014-0539-x) · PMC4253000.
26. ENVO:01001176, ENVO:01001002, ENVO:01001055, ENVO:01001000, FOODON:03414466, BTO:0000090, UBERON:0009719, NCBITaxon:7712 — labels, definitions and subclass edges verified against this repo's `data/raw/ontology_terms.tsv` and `data/raw/ontology_subclass_edges.tsv`, cross-checked at [EBI OLS4](https://www.ebi.ac.uk/ols4/).

### What in this report is inference, not a cited claim

Flagged explicitly, because these must not enter the ontology as if sourced:

- **That `Host-associated > Invertebrates > Tunicates` and `Host-associated > Tunicates` denote the same thing.** No source states this. It is my inference from identical labels, identical source vocabulary, an empty assertion count on this path, and GOLD's documented non-exhaustive, incrementally-curated term list. It is the report's central recommendation and the curator should treat it as a judgement to confirm, not a fact to cite.
- **That an abandoned larvacean house falls outside the concept.** A boundary decision, not a finding. Davoll & Silver document the house's microbial community; nobody has ruled on whether it counts as host-associated.
- **The compartment table's framing** ("each is a distinct habitat") is my synthesis; each row's numbers are sourced, but no single paper enumerates tunicate compartments as habitat sub-types.
- **That ENVO:01001176's "aquatic" restriction is safe here because tunicates are exclusively marine** — the exclusivity is sourced (refs 3, 4), the fitness-for-genus conclusion is mine.
- **I did not find a dedicated microbiome study of salps (Thaliacea: Salpida) or larvaceans.** Searches returned diet/gut-contents work for *Thalia democratica* and *Salpa fusiformis* and house-aggregate ecology for *Oikopleura*, but no 16S survey. The pelagic evidence in this report rests on pyrosomes. If the definition claims anything about the clade as a whole, that gap is real — pyrosomes and ascidians carry it.
- **No review article specifically on the tunicate holobiont surfaced** in searches; all microbiome citations above are primary research.

---

## 5. Synonyms, and what not to conflate

**Names in real use for the concept (subphylum-level):**
- Tunicata (Lamarck, 1816) — current
- Urochordata / urochordates — historical, still widespread; explicitly given as the former name in FOODON:03414466's own text
- tunicate-associated environment / tunicate holobiont — the habitat sense
- "sea squirts" — very common but see below

**Vernaculars for sub-groups (narrower, not synonyms of this term):** sea squirt, sea pork, ascidian (Ascidiacea); salp, doliolid, pyrosome (Thaliacea); larvacean, appendicularian, *Oikopleura* (Appendicularia); sea pineapple, 멍게 (meongge), ホヤ (hoya) for *Halocynthia roretzi*.

**Wrongly treated as the same thing:**

| Conflation | Why it is wrong |
|---|---|
| **"Tunicates" = "sea squirts"/ascidians** | The commonest error, and it is *in the corpus already* as a real child record: `Ascidians` (`GOLD.34c28836da`, 79 organisms) is class Ascidiacea only. Thaliaceans and appendicularians are tunicates and are not sea squirts. |
| **Tunicates ↔ non-chordate invertebrates** | GOLD's `Invertebrates` parent invites this. Tunicates are chordates and vertebrates' closest living relatives (ref 2). "Invertebrate" is true only as a paraphyletic grade. |
| **Tunicate ↔ the taxon Tunicata** | The habitat is the animal-as-place; the taxon is a class of organisms. Keep NCBITaxon:7712 / FOODON:03414466 as `relation: xref`, per #99 and #114. |
| **Tunicate ↔ tunic** | The tunic is one compartment of the animal; the concept covers gut, branchial sac and cloacal cavity too — which the compartment-comparison data show are microbially distinct (ref 6). |
| **The tunicate ↔ the drug/metabolite producer** | ET-743 is "from *Ecteinascidia turbinata*" throughout the pharmacology literature; the producer is a bacterial endosymbiont (ref 12). Same for patellamides and *Prochloron* (refs 10, 11). Relevant because characteristic-taxa fields can otherwise inherit the host as the source organism. |
| **Tunicate ↔ its food/product** | `Halocynthia roretzi` as an edible commodity belongs in FOOD, not here. FOODON:03414466 sits in a food ontology precisely for that reading. |
| **"Salp" ↔ "salping-" anatomy terms** | A lexical trap for automated matching: the slice contains `salpinges`/`salpingopharyngeal` (UBERON:0003889, BTO:0001048) as fallopian-tube and pharyngeal-muscle synonyms. Nothing to do with Thaliacea. |
| **Ascidian ↔ PO's "ascidia"** | `PO:0009025` *vascular leaf* carries "ascidia/ascidium" as narrow synonyms (pitcher leaves). Another lexical false friend in the slice. |

---

## 6. Should this be a term at all?

**Two answers, and they differ.**

**Is "Tunicates" a habitat? Yes — unambiguously.** It is a place where microbes live, at every scale from an intracellular endosymbiont with a 0.6 Mb genome to a metre-scale colony surface biofilm, with communities that are measurably distinct from the surrounding seawater and correlate with host phylogeny. The prior `NOT_APPLICABLE` was wrong for exactly the reason the curation note gives, and the note's reasoning matches this evidence. `CONFIRM_UNGROUNDED` + an ENVO term request for *tunicate-associated environment* is the right disposition for the concept — consistent with how Sponge, Nematoda, Reptilia, Mammals, Birds and Fish are handled.

**Should *this record* carry that term? Probably not — it should be `SAME_AS habitatmech:GOLD.78c645fff9`.** This is the reading I would defend: `Host-associated > Invertebrates > Tunicates` is a duplicate placement of the concept `Host-associated > Tunicates`, carrying zero assertions and no children, while the other path carries 23 organisms and the entire Ascidians subtree. Publishing two records with the same label, the same xref, the same note and one definition text between them is a defect the corpus has a mechanism for. If the SAME_AS is taken, the surviving record `GOLD.78c645fff9` gets the definition sentence at the top of this report, and everything in §§1–5 supports it.

If the curator instead keeps both records, then the honest position is that they are word-for-word the same concept and must carry word-for-word the same definition — and the report offers no differentia that could separate them, because the sources contain none.

**Two smaller changes worth making either way:**

1. **Add `ENVO:01001176` as a parent** (`relation: parent`) alongside the existing GOLD-invertebrates parent. It is genuinely broader, its two conditions are clade-universal for Tunicata, and the crustacean objection to it does not apply here.
2. **Consider `NCBITaxon:7712` as the taxon xref.** `FOODON:03414466` currently serves as both "nearest broader term" and taxon pointer, but its definition text describes the animals and it lives in a food ontology. NCBITaxon:7712 is in the vendored slice and says exactly what the xref is meant to say. Keep the FOODON link as an additional xref — it records what upstream saw — but it should not be doing the work of naming the clade.

## Citations

1. https://academic.oup.com/nar/article/51/D1/D957/6786204
2. https://www.nature.com/articles/nature04336
3. https://pubmed.ncbi.nlm.nih.gov/16495997/
4. https://pubmed.ncbi.nlm.nih.gov/29330139/
5. https://onlinelibrary.wiley.com/doi/full/10.1111/cla.12405
6. https://www.nature.com/articles/ismej2013188
7. https://enviromicro-journals.onlinelibrary.wiley.com/doi/full/10.1111/1758-2229.13242
8. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0093386
9. https://pubmed.ncbi.nlm.nih.gov/28082961/
10. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510431/
11. https://enviromicro-journals.onlinelibrary.wiley.com/doi/abs/10.1111/1462-2920.12908
12. https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2021.606818/full
13. https://www.nature.com/articles/s43705-021-00007-1
14. https://link.springer.com/article/10.1007/s00227-017-3174-1
15. https://www.int-res.com/abstracts/meps/v33/p111-120/
16. https://pubmed.ncbi.nlm.nih.gov/24991851/
17. https://doi.org/10.3390/genes10040294
18. https://royalsocietypublishing.org/doi/10.1098/rspb.2016.1712
19. https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2020.00201/full
20. https://www.nature.com/articles/s41598-017-11441-4
21. https://www.pnas.org/doi/10.1073/pnas.0501424102
22. https://www.pnas.org/content/108/51/E1423
23. https://news.umich.edu/pinpointing-natural-cancer-drug-s-true-origins-brings-sustainable-production-a-step-closer/
24. https://www.nature.com/articles/s41598-020-73446-w
25. https://hal.science/halsde-00315436/document
26. https://www.osti.gov/pages/biblio/1344906
27. https://link.springer.com/article/10.1186/s12915-024-01872-7
28. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7694362/
29. https://link.springer.com/article/10.1186/s13071-014-0539-x
30. https://www.ebi.ac.uk/ols4/