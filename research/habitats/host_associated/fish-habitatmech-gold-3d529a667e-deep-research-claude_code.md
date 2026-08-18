---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:09:11.653168'
end_time: '2026-08-17T16:14:51.356214'
duration_seconds: 339.7
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Fish
  habitat_identifier: habitatmech:GOLD.3d529a667e
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Fish'
  assertions: '1350'
  parent_terms: ENVO:01001000, ENVO:01001002
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001002 ''animal-associated environment'' attached as a parent.
    Fish as host. Parented to animal-associated environment; not grounded there because
    every host clade would merge onto one record. ENVO term request. (source concept
    habitatmech:GOLD.3d529a667e)'
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
  - claude-opus-5
  web_search_requests: 15
  num_turns: 24
  total_cost_usd: 2.6529579999999995
  session_id: 57fd0885-efa6-4a23-b3de-7bbe0499f515
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 21
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Fish
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.3d529a667e
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Fish
- **Upstream assertion volume:** 1350
- **Nearest broader term already on the record:** ENVO:01001000, ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Fish as host. Parented to animal-associated environment; not grounded there because every host clade would merge onto one record. ENVO term request. (source concept habitatmech:GOLD.3d529a667e)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Fish** as a microbial habitat, with citations.

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

# Fish (`habitatmech:GOLD.3d529a667e`) — definition research

> **Proposed definition:** An animal-associated environment which is determined by a living fish — a gill-bearing, ectothermic aquatic craniate lacking digit-bearing limbs — whose gut lumen, skin mucus and gill surfaces are in continuous exchange with the surrounding water yet sustain microbiota compositionally distinct from it.

Genus term: `ENVO:01001002` *animal-associated environment* (already the record's parent). The differentia is the host clade plus the one property that separates fish hosts from every other animal-associated sibling: the host lives submerged, so its colonisable surfaces are perfused by, and ectothermically equilibrated with, ambient water.

---

## 1. What the concept denotes

**The thing sampled is a live (or freshly killed) fish, and specifically the microbial habitat its body provides** — intestinal digesta and gut mucosa, skin mucus, and gill tissue/mucus. The GOLD path `Host-associated > Fish` places the concept at GOLD's Ecosystem Category level, directly under the `Host-associated` Ecosystem; GOLD's lower levels (Ecosystem Type / Subtype / Specific Ecosystem) then carry the organ (digestive system, gills, skin) ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); [Mukherjee et al. 2019, GOLD v.7, *NAR* 47:D649](https://pubmed.ncbi.nlm.nih.gov/30357420/)). So the concept is the **whole host organism as a place**, sitting one level above the organ-specific records.

**Inside the concept:** any non-tetrapod aquatic craniate acting as host — hagfishes and lampreys, cartilaginous fishes, ray-finned fishes, non-tetrapod lobe-finned fishes — wild or farmed, marine or freshwater; and the microbial communities of its gut, skin mucus, gills and internal organs.

**Outside the concept (neighbouring records):**
- the **water or sediment** the fish lives in — `Environmental > Aquatic` in GOLD; ENVO aquatic biomes. Distinctness from the water column is empirically demonstrated, not assumed (see §3).
- the **rearing infrastructure** — `ENVO:00000294` *fish farm*, `ENVO:00000056` *fishpond*, `ENVO:00000295` *fish hatchery*, `ENVO:01000928` *fish processing building*. These are facilities and constructed water bodies, not the animal ([OLS/ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo)).
- **fish organs as habitats** — `gut`, `skin`, `gill`. Under this repo's part/whole rule these ground to UBERON anatomy terms; the whole-organism concept does not, which is exactly why this record exists.
- **fish as food** — fillet, fish meal, fermented fish products (FOODON). A dead processed product is a food material, not a host.

**Ambiguity.** The label "Fish" carries three readings; the source path resolves it:
1. *the host organism as a habitat* — what `Host-associated > Fish` means, and the reading this record takes;
2. *the taxonomic grouping* — a vernacular, **paraphyletic** grouping, not a clade (any clade containing all fishes also contains tetrapods; the old class Pisces is not used in modern taxonomy) ([Miya & Nishida-style genomic reconsideration, *Ichthyological Research* 2023, doi:10.1007/s10228-023-00939-9](https://link.springer.com/article/10.1007/s10228-023-00939-9));
3. *fish as a commodity/food*, which in fisheries usage sometimes stretches to shellfish — not the GOLD reading.

A fourth, purely lexical: **FISH = fluorescence in situ hybridisation** (`OBI:0003094`). Irrelevant semantically, but a real collision when text-mining source labels.

## 2. Genus — the broader kind

**Recommended genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal", with ancestors `ENVO:01001000` *environmental system determined by an organism* → `ENVO:01000254` *environmental system* (verified via [OLS4 hierarchicalAncestors for ENVO:01001002](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002)). Synonyms include "Metazoan-associated environment"; it is in the envoEmpo subset mapped to EMPO "Animal".

**No ENVO term names fish-as-habitat.** An OLS search of ENVO for "fish" returns only facilities, gear and processes (`fish farm`, `fishpond`, `fish hatchery`, `fish processing building`, `fishing` `ENVO:06105113`, `ghost fishing`, `fishing gear` terms). There is no `fish-associated environment`, and I found no open ENVO new-term request for one; the nearest discussion is [ENVO issue #1029, "EnvO terms for host-associated samples"](https://github.com/EnvironmentOntology/envo/issues/1029) (opened 20 Oct 2020, closed), which requested host-/animal-/human-/plant-associated biome terms.

**Near-misses and why each fails:**

| Term | Why it is not a match |
|---|---|
| `ENVO:01001002` animal-associated environment | **Too broad** — the genus, not the species. Grounding here merges every host clade (fish, birds, mammals, insects) onto one record, which is the curator's stated reason for leaving it as parent only. |
| `ENVO:01001055` environment associated with an animal part or small animal | Asserts *part-hood* or a *small whole animal*. A fish is a whole animal and mostly not small; this term is the right home for the *gut / skin / gill* child records, not the host. |
| `ENVO:01001176` environment associated with an aquatic invertebrate | Right medium, wrong clade — fishes are vertebrates. Explicitly "lacks a vertebral column". |
| `ENVO:01001179` cnidarian-associated environment | Not a match, but the **strongest precedent**: ENVO already mints clade-scoped associated-environment classes below animal-associated environment. A `fish-associated environment` request is consistent with existing ENVO practice, not a novel pattern. |
| `ENVO:01001041` fungi-associated environment / `ENVO:01001001` plant-associated environment | Sibling pattern only; wrong kingdom. |
| `FOODON:03411222` *fish* — "gill-bearing aquatic craniate animals that lack limbs with digits" | An **organism/food-material** term, not an environment. Its *textual definition* is the best available genus-differentia phrasing for the host and is worth reusing as wording; it is not a grounding target. (Surfaced via OLS through FOBI, which imports FOODON — the curator should confirm the ID and label in the vendored slice before citing it, per this repo's label-match gate.) |
| NCBITaxon | **No node exists.** OLS returns no NCBITaxon term labelled "fish", "fishes" or "Pisces" — only viruses, specimen-level entries and `Fish10K` assemblies. Because the group is paraphyletic, the nearest single taxa are each wrong: `Actinopterygii` excludes sharks and lampreys; `Euteleostomi`/`Vertebrata` includes tetrapods. **This means the usual `relation: xref` to a taxon term is unavailable for this record** — an inference, but a firm one. |

## 3. Differentia — what distinguishes it from its animal-associated siblings

Each of these is observable/measurable and separates fish hosts from bird, mammal, insect or plant hosts:

1. **Submerged host: mucosal surfaces are in continuous contact with the ambient water column.** Aquatic environments host far denser and more dynamic microbial suspensions than air, so fish external surfaces face continuous microbial exposure that terrestrial hosts do not ([McMurtrie et al. 2025, *FEMS Microbiol Rev* 49:fuaf027, doi:10.1093/femsre/fuaf027](https://doi.org/10.1093/femsre/fuaf027)).
2. **Yet the communities are host-selected, not a water sample.** In 282 wild specimens across 50 tropical marine species (31 families), gut digesta microbiota was distinct from surrounding water — only 3 of ~18–19 core genera were shared with water ([Soh et al. 2024, *npj Biofilms Microbiomes* 10:11, doi:10.1038/s41522-024-00484-x](https://doi.org/10.1038/s41522-024-00484-x)). On skin, only ~3% of variation in coral-reef fish skin composition was explained by reef habitat, and *Vibrio* rises from ~1.7% of water microbiota to ~26% of skin microbiota (McMurtrie et al. 2025).
3. **Three quasi-independent body-site habitats — gut, skin mucus, gill — with body site the strongest driver of community structure.** Across 101 Southern California marine fish species (22 orders, 55 families), body site dominated microbial diversity and biomass; midgut, gill and skin together harbour up to 5.5× the microbial diversity of the hindgut ([Minich et al. 2022, *Nat Commun* 13:6978, doi:10.1038/s41467-022-34557-2](https://doi.org/10.1038/s41467-022-34557-2)).
4. **Ectothermy: habitat temperature tracks the water, and osmotic regime tracks salinity.** Temperature, salinity and pH are recognised drivers of fish gut community composition; external microbiomes are especially susceptible to temperature variation while gut microbiomes are especially susceptible to salinity change ([Xavier et al. 2024, *Reviews in Aquaculture* 16, doi:10.1111/raq.12862](https://doi.org/10.1111/raq.12862); [Egerton et al. 2018, *Front Microbiol* 9:873, doi:10.3389/fmicb.2018.00873](https://doi.org/10.3389/fmicb.2018.00873)).
5. **Characteristic taxonomic signature, different from mammal hosts.** Proteobacteria dominate the fish GI tract (with Bacteroidetes and Firmicutes, ~90% of fish intestinal microbiota reported to date), unlike the Bacteroidetes/Firmicutes-dominated mammalian gut; Fusobacteria (e.g. *Cetobacterium*) are characteristic of freshwater fishes, *Vibrio*/*Photobacterium* of marine carnivores, and *Mycoplasma* of salmonids (Egerton et al. 2018; [Wang et al. 2018, *Rev Aquac* 10:626, doi:10.1111/raq.12191](https://doi.org/10.1111/raq.12191)).
6. **Low microbial biomass relative to endotherm hosts.** Fish intestines carry substantially lower microbial biomass than warm-blooded animals, with samples often >90% host DNA ([Thormar et al. 2024, *Ecol Evol* 14, doi:10.1002/ece3.70302](https://doi.org/10.1002/ece3.70302)). Reported gut densities span ~10⁴–10⁹ CFU g⁻¹ by culture and 10⁷–10¹¹ cells g⁻¹ by molecular counts, rising from stomach to posterior intestine (Egerton et al. 2018; Wang et al. 2018).
7. **Largely uncultured and undersampled.** ~97% of fish-associated microorganisms have no cultured representative (68.1% of ASVs lack a cultured genus-level representative), and only a small fraction of >32,000 known fish species have had gut microbiota examined (Soh et al. 2024). In a 569-species vertebrate hindgut meta-analysis, fishes had the highest percentage of unique microbial taxa (92%) (Minich et al. 2022).
8. **Fish-specific mucosal immunity shapes the community.** Secretory IgT coats the majority of bacterial residents on fish skin and gills; mucin glycosylation patterns bind bacterial lectins and mediate selection (McMurtrie et al. 2025).

**Scale of the concept (why one record is defensible but internally heterogeneous):** FishBase covers >36,500 species; Eschmeyer's Catalog records ~37,678 valid species ([FishBase](https://www.fishbase.se/home.htm); [Eschmeyer's Catalog of Fishes](https://researcharchive.calacademy.org/research/ichthyology/catalog/fishcatmain.asp)). *My inference:* the definition should therefore state the host kind and the water-exchange property, and **not** assert a uniform microbiota, since composition splits sharply along marine/freshwater and wild/farmed lines.

## 4. Sources

- Egerton S, Culloty S, Whooley J, Stanton C, Ross RP (2018). The Gut Microbiota of Marine Fish. *Front Microbiol* 9:873. doi:[10.3389/fmicb.2018.00873](https://doi.org/10.3389/fmicb.2018.00873) — PMID 29780377.
- Minich JJ, Härer A, Vechinski J, et al. (17 Nov 2022). Host biology, ecology and the environment influence microbial biomass and diversity in 101 marine fish species. *Nat Commun* 13:6978. doi:[10.1038/s41467-022-34557-2](https://doi.org/10.1038/s41467-022-34557-2) — PMID 36396943.
- Soh M, Tay YC, Lee CS, Low A, Orban L, Jaafar Z, Seedorf H (2024). The intestinal digesta microbiota of tropical marine fish is largely uncultured and distinct from surrounding water microbiota. *npj Biofilms Microbiomes* 10:11. doi:[10.1038/s41522-024-00484-x](https://doi.org/10.1038/s41522-024-00484-x) — [PMC10876542](https://pmc.ncbi.nlm.nih.gov/articles/PMC10876542/).
- McMurtrie J, Bell AG, Cable J, Temperton B, Tyler CR (2025). The ecology and plasticity of fish skin and gill microbiomes: seeking what matters in health and disease. *FEMS Microbiol Rev* 49:fuaf027. doi:[10.1093/femsre/fuaf027](https://doi.org/10.1093/femsre/fuaf027) — [PMC12218203](https://pmc.ncbi.nlm.nih.gov/articles/PMC12218203/).
- Xavier R, et al. (2024). Signatures of dysbiosis in fish microbiomes in the context of aquaculture. *Reviews in Aquaculture*. doi:[10.1111/raq.12862](https://doi.org/10.1111/raq.12862).
- Wang AR, Ran C, Ringø E, Zhou ZG (2018). Progress in fish gastrointestinal microbiota research. *Rev Aquac* 10:626–640. doi:[10.1111/raq.12191](https://doi.org/10.1111/raq.12191).
- Thormar EA, et al. (2024). Sampling fish gut microbiota — a genome-resolved metagenomic approach. *Ecol Evol* 14. doi:[10.1002/ece3.70302](https://doi.org/10.1002/ece3.70302) — [PMC11407903](https://pmc.ncbi.nlm.nih.gov/articles/PMC11407903/).
- Sylvain F-É, et al. (2020). Fish Skin and Gut Microbiomes Show Contrasting Signatures of Host Species and Habitat. *Appl Environ Microbiol* 86:e00789-20. doi:[10.1128/AEM.00789-20](https://doi.org/10.1128/AEM.00789-20) — PMID 32503908.
- Mukherjee S, et al. (2019). Genomes OnLine Database (GOLD) v.7. *Nucleic Acids Res* 47:D649–D659 — [PMID 30357420](https://pubmed.ncbi.nlm.nih.gov/30357420/); classification docs: <https://gold.jgi.doe.gov/ecosystem_classification>.
- ENVO terms verified via EMBL-EBI OLS4: `ENVO:01001002`, `ENVO:01001000`, `ENVO:01001055`, `ENVO:01001176`, `ENVO:01001179`, `ENVO:01001041`, `ENVO:01001001`, `ENVO:00000294`, `ENVO:00000056`, `ENVO:00000295`, `ENVO:01000928` — <https://www.ebi.ac.uk/ols4/ontologies/envo>. ENVO term-request conventions (genus-differentia; definition citations required in the issue): [ENVO wiki, Creating good definitions](https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions) and [ENVO issue #1029](https://github.com/EnvironmentOntology/envo/issues/1029).
- Paraphyly of "fish": [Ichthyological Research (2023), doi:10.1007/s10228-023-00939-9](https://link.springer.com/article/10.1007/s10228-023-00939-9). Species counts: [FishBase](https://www.fishbase.se/home.htm), [Eschmeyer's Catalog of Fishes](https://researcharchive.calacademy.org/research/ichthyology/catalog/fishcatmain.asp).

**Explicitly flagged as my inference, not source statements:** (a) that no NCBITaxon xref target exists for "fish" and that the usual taxon-xref slot must therefore be left empty or filled with a non-taxonomic reference; (b) that the definition should avoid asserting a uniform microbiota across the group; (c) that `ENVO:01001179` *cnidarian-associated environment* constitutes precedent supporting a fish-scoped ENVO request — ENVO has not stated this. I did **not** find an enumerated list of GOLD's `Host-associated > Fish` child paths; the browsable tree at <https://gold.jgi.doe.gov/ecosystemtree> is the place to confirm which organ subtypes feed this record's 1,350 assertions.

## 5. Synonyms, and what not to conflate

**In real use as names for this concept:** fish-associated environment; fish-associated habitat; fish host; piscine host; fish holobiont (host + microbiota framing, common in aquaculture literature); fish mucosal environment (covers skin/gill/gut collectively); finfish (fisheries usage, explicitly excluding shellfish). EMPO maps this region to "Animal" with EMPO-3 levels *Animal surface* / *Animal distal gut* / *Animal secretion*. Narrower, frequently used as if equivalent: **teleost** (bony fishes only — excludes sharks, rays, lampreys, hagfish; >28,000 species).

**Commonly but wrongly treated as the same thing:**
- **Pisces / "class Pisces"** — an obsolete rank for a paraphyletic group; not a valid taxon and not an ontology grounding target.
- **Actinopterygii (`NCBITaxon:7898`)** — ray-finned fishes only; using it as identity silently drops Chondrichthyes and cyclostomes.
- **Shellfish / molluscs / crustaceans** — included by "fish" in some fisheries and dietary usage; these fall under `ENVO:01001176` *environment associated with an aquatic invertebrate*, a different branch.
- **Fish organs** — gut, gill, skin. Under this repo's rule these are *parts* and ground to UBERON anatomy; conflating them with the host record collapses the body-site structure that is the single strongest driver of community composition (Minich et al. 2022).
- **The water the fish lives in** — aquarium water, pond water, seawater. Empirically a different community (Soh et al. 2024).
- **Aquaculture infrastructure** — fish farm, fishpond, hatchery, RAS tank biofilm. Built environments; ENVO has terms for them already.
- **Fish as food or feed** — fillet, fish meal, fermented fish (FOODON territory); a food material, not a host.
- **Fish diseases and pathogens** — furunculosis, *Photobacterium damselae* infection. Disease states are not habitats and are `NOT_APPLICABLE` territory in this corpus.
- **FISH (fluorescence in situ hybridisation)**, `OBI:0003094` — string collision only.

## 6. Should it be a term at all?

**Yes — mint it, do not mark it `NOT_APPLICABLE`.**

Fish here is an organism *acting as a host*, i.e. the place where microbes live, which is exactly what ENVO models at plant-/animal-/fungi-associated environment. Under this repo's rule (`CLAUDE.md`: "An organism acting as a host IS a habitat; the taxon term is not"), the concept keeps its own minted identity as a term-request candidate. The literature treats fish as a habitat in precisely this sense: as a set of colonisable, host-selected mucosal surfaces with measurable biomass, characteristic taxa and environmental drivers (Minich et al. 2022; McMurtrie et al. 2025; Soh et al. 2024). 1,350 GOLD assertions confirm it is a real sampling context, not an artefact.

Two record-shaping consequences:

1. **Parenting to `ENVO:01001002` is correct; grounding to it is not** — the term is genuinely broader, and grounding would merge fish with birds, mammals and insects onto one record. The curator's existing note is sound.
2. **The taxon-xref slot has no valid filler.** Unlike `Mollusca` or `Porifera`, where `relation: xref` to the clade term records what upstream saw, "Fish" corresponds to no NCBITaxon node because the grouping is paraphyletic. Options, in my order of preference: leave the xref empty and say why in the note; or xref `FOODON:03411222` *fish* purely as a lexical cross-reference (verify ID + label against the vendored slice first — this repo's label-match gate will reject it otherwise). Do **not** substitute `Actinopterygii` for the whole group.

The one genuine weakness to record in the note: this is a ~37,000-species, marine-and-freshwater, wild-and-farmed grouping held together by a vernacular category rather than a clade. That is an argument for keeping the differentia to host kind + submerged-mucosal-exchange, and for letting the organ-level and marine/freshwater distinctions live in child records — not an argument against the term.

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://pubmed.ncbi.nlm.nih.gov/30357420/
3. https://www.ebi.ac.uk/ols4/ontologies/envo
4. https://link.springer.com/article/10.1007/s10228-023-00939-9
5. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001002
6. https://github.com/EnvironmentOntology/envo/issues/1029
7. https://doi.org/10.1093/femsre/fuaf027
8. https://doi.org/10.1038/s41522-024-00484-x
9. https://doi.org/10.1038/s41467-022-34557-2
10. https://doi.org/10.1111/raq.12862
11. https://doi.org/10.3389/fmicb.2018.00873
12. https://doi.org/10.1111/raq.12191
13. https://doi.org/10.1002/ece3.70302
14. https://www.fishbase.se/home.htm
15. https://researcharchive.calacademy.org/research/ichthyology/catalog/fishcatmain.asp
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC10876542/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC12218203/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC11407903/
19. https://doi.org/10.1128/AEM.00789-20
20. https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions
21. https://gold.jgi.doe.gov/ecosystemtree