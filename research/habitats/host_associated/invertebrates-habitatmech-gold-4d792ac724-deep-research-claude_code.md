---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T16:28:51.529886'
end_time: '2026-08-17T16:35:34.536725'
duration_seconds: 403.01
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Invertebrates
  habitat_identifier: habitatmech:GOLD.4d792ac724
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Invertebrates'
  assertions: '621'
  parent_terms: ENVO:01001000, ENVO:01001002
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Nearest
    broader term ENVO:01001002 ''animal-associated environment'' attached as a parent.
    Invertebrates as host. Parented to animal-associated environment; not grounded
    there because every host clade would merge onto one record. ENVO term request.
    (source concept habitatmech:GOLD.4d792ac724)'
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
  web_search_requests: 13
  num_turns: 30
  total_cost_usd: 2.910074
  session_id: 99348380-60db-4305-a6a8-2fdee7268967
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 22
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Invertebrates
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.4d792ac724
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Invertebrates
- **Upstream assertion volume:** 621
- **Nearest broader term already on the record:** ENVO:01001000, ENVO:01001002
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term ENVO:01001002 'animal-associated environment' attached as a parent. Invertebrates as host. Parented to animal-associated environment; not grounded there because every host clade would merge onto one record. ENVO term request. (source concept habitatmech:GOLD.4d792ac724)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Invertebrates** as a microbial habitat, with citations.

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

I'll research this now.

# Invertebrates — `habitatmech:GOLD.4d792ac724`

> **Proposed definition:** An animal-associated environment which is determined by a host animal that lacks a vertebral column.

Compact ENVO-pattern variant, matching the wording of the parent term `ENVO:01001002` ("An environmental system determined by an animal."):

> An environmental system determined by a metazoan that lacks a vertebral column.

The second form is what `curation/term_requests.tsv` already carries for this identifier ("An environmental system determined by an invertebrate."), except that it avoids defining "invertebrate" by the word "invertebrate". The differentia is deliberately privative — see §3 for why that is defensible here and how ENVO itself has already accepted it.

---

## 1. What the concept denotes

**The thing sampled.** The body of a living (or recently dead) animal outside the subphylum Vertebrata, considered as the physical setting a microbial sample is taken from: its gut lumen and gut wall, body surface and cuticle, mucus layer, hemolymph and body cavity, specialised symbiont-bearing organs (bacteriomes, light organs, nematode receptacles), and whole homogenised small bodies. It is the host-as-place, not the host as a taxonomic class.

**What is inside.** Every metazoan phylum except Vertebrata: sponges, cnidarians, ctenophores, flatworms, nematodes, annelids, molluscs, arthropods, bryozoans, echinoderms, and the invertebrate chordates (tunicates, cephalochordates).

**What is outside — the neighbouring concepts.**

| Neighbour | Relationship |
|---|---|
| `ENVO:01001002` animal-associated environment | broader — includes vertebrate hosts |
| Vertebrate host categories (GOLD *Fish*, *Mammals*, *Birds*, *Reptilia*, *Amphibia*) | disjoint siblings |
| GOLD *Host-associated > Plants / Fungi / Algae / Protists / Amoebozoa / Microbial* | disjoint — non-animal hosts |
| Anatomical parts of an invertebrate (`gut`, `mucus`, `tissue`) | narrower, and per this repo's rule those **ground** to UBERON/ENVO anatomy terms rather than staying here |
| Environment *around* an invertebrate (coral reef `ENVO:01000281`, sponge ground) | different concept — a biome/geographic feature, not a host-determined system |

**The ambiguity that must not be resolved silently.** The label supports two readings, and the source data supports both at once:

- **Reading A — the plain meaning.** All animals lacking a vertebral column. This is what the 621 assertions at the bare node mean: organisms whose GOLD path terminates at `Host-associated > Invertebrates` with no ecosystem type, i.e. the host was recorded only as "an invertebrate".
- **Reading B — GOLD's residual bucket.** Extensionally, in GOLD's own tree the *Invertebrates* category holds only Cnidaria, Nematoda, Echinodermata, Platyhelminthes, Bryozoans, Ctenophora, Tunicates and a bare `Tissue` node, because **Arthropoda, Mollusca, Porifera and Annelida were promoted to sibling ecosystem categories directly under `Host-associated`** (verified in `data/raw/gold_ecosystem_paths.tsv`; GOLD documents that its categories "can be individual hosts or phyla" and that paths are "primarily driven by the samples curated" rather than being a complete taxonomy — <https://gold.jgi.doe.gov/ecosystem_classification>).

**Recommendation:** define reading A and record reading B as a curation note. GOLD's promotion of Arthropoda and Porifera to top-level categories is a data-management artefact of sample volume, not a claim that arthropods are not invertebrates; a definition written to reading B would be undefinable in any vocabulary but GOLD's, and would break the moment GOLD promotes another phylum. The cost is that in HabitatMech's parent graph, `Arthropoda`, `Mollusca` and `Porifera` will not sit under this record even though the definition covers them — that is a fidelity-to-source artefact worth stating on the record.

*Counts note:* 621 is the count at the node itself, not cumulative — its children `Cnidaria > Coral` (382) and `Nematoda` (300) already exceed it. That is my inference from the table's column structure, not a GOLD-documented statement.

## 2. Genus — the broader kind

**Genus: `ENVO:01001002` "animal-associated environment"** — "An environmental system determined by an animal." (<http://purl.obolibrary.org/obo/ENVO_01001002>; ENVO: Buttigieg et al., *J Biomed Semantics* 2013, [doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43); Buttigieg et al., *J Biomed Semantics* 2016, [doi:10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6)).

This is already the record's parent and it is the right genus. It has only three asserted direct children in ENVO today (checked via OLS4, `hierarchicalChildren` of `ENVO_01001002`): `ENVO:01001176`, `ENVO:01001179`, and `ENVO:01001829` — the branch is extremely sparse, which is why nothing at the right level of generality exists.

### Near-misses, and why each fails

| Candidate | Why it is not a match |
|---|---|
| **`ENVO:01001176` "environment associated with an aquatic invertebrate"** — *"An environment which has its properties and composition largely determined by the presence of a metazoan which lacks a vetebral column and which has a habitat that is found in an aquatic environmental system."* ([OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176)) | **The closest term in any vocabulary, and strictly narrower.** It adds an aquatic-habitat restriction the GOLD concept does not make — GOLD's node covers terrestrial nematodes, entomopathogenic-nematode hosts and soil invertebrates as readily as corals. Grounding here would silently assert every one of the 621 organisms came from an aquatic host. **This term is the single strongest piece of evidence for the definition**: ENVO has already committed to "a metazoan which lacks a vertebral column" as the differentia, so the requested term is simply that clause without the aquatic conjunct, and `ENVO:01001176` becomes its subclass. (Note the typo "vetebral" in the live ENVO definition.) |
| **`ENVO:01001055` "environment associated with an animal part or small animal"** — *"An environmental system determined by part of a living or dead animal, or a whole small animal."* | Different axis. It is about parthood and body size, not phylogeny; it covers vertebrate parts, and its "small animal" clause excludes a giant squid or a *Architeuthis*-scale host. It is a *parent* of `ENVO:01001176`, not a synonym for the concept. |
| **`ENVO:01001179` "cnidarian-associated environment"** | Narrower — one phylum among ~30. Its existence is precedent that ENVO accepts host-clade-keyed environment terms. |
| **`ENVO:01001000` "environmental system determined by an organism"** (synonym: *host-associated environment*) | Two levels too broad; already on the record as a grandparent. |
| **UBERON / BTO / NCBITaxon "Invertebrata"** | **No such term exists.** An OLS4 exact-label search across NCBITaxon, UBERON and BTO for `Invertebrata`/`invertebrate` returns nothing (only `UBERON:0003917` "arthropod fat body", via the synonym "fat body sensu invertebrata"). NCBI Taxonomy does not carry Invertebrata because it is not a clade. **This is materially different from every other host-clade case in this corpus** (Mollusca, Porifera, Nematoda all have NCBITaxon terms available for `relation: xref`): here there is no taxon term to xref, so nothing at all in the ontology landscape names the concept. |
| `NCIT:C17649` "Other" (the upstream lexical match for BacDive *Invertebrates-Other*) | A bucket with no content of its own; already rejected on `habitatmech:BACDIVE.e864a16f03`. |

## 3. Differentia — what distinguishes it

The primary differentia is **the phylogenetic position of the determining host: it lacks a vertebral column** (Britannica, *invertebrate*: any animal lacking a vertebral column, in contrast to cartilaginous or bony vertebrates — <https://www.britannica.com/animal/invertebrate>).

This differentia is privative, which is normally a weakness in an Aristotelian definition. Three things make it defensible here:

1. **The category is genuinely privative.** Invertebrata is a paraphyletic grade, not a clade — tunicates and cephalochordates are closer to vertebrates than to other invertebrates, and the group's members span ≥30 phyla whose most recent common ancestor is the base of Metazoa ([Wikipedia, *Invertebrate*](https://en.wikipedia.org/wiki/Invertebrate); on grades vs clades, [Wikipedia, *Paraphyly*](https://en.wikipedia.org/wiki/Paraphyly)). A positive differentia would be false: no character is shared by sponges, nematodes and squid to the exclusion of fish.
2. **ENVO has already made the same move** in `ENVO:01001176`.
3. **The alternative is worse.** Refusing the term leaves 621 GOLD organism annotations (plus BacDive's 596 sources / 507 strains under *Invertebrates-Other*) with no representable habitat.

**Secondary, observable properties of the habitat** (these belong in a comment or elucidation, not the definition sentence, because they hold with exceptions):

- **No adaptive immunity.** Invertebrates lack conventional antibody-based immunity and rely on innate recognition — PGRPs, GNBPs, TLRs, LBPs — to discriminate and maintain symbionts. This is the single best-attested functional difference between invertebrate and vertebrate host habitats, and it shapes community assembly. Nyholm & Graf, *Nat Rev Microbiol* 10:815–827 (2012), [doi:10.1038/nrmicro2894](https://doi.org/10.1038/nrmicro2894), PMID 23147708. A 2024 synthesis for marine invertebrates: [PMC11359984](https://pmc.ncbi.nlm.nih.gov/articles/PMC11359984/).
- **Simpler, lower-diversity communities.** Invertebrate hosts "associate with fewer microbes", which is precisely why they are used as tractable host–microbe models. Petersen & Osvatic, *mSystems* 3(2):e00179-17 (2018), [doi:10.1128/mSystems.00179-17](https://doi.org/10.1128/mSystems.00179-17), PMID 29556539.
- **Ectothermy.** Habitat temperature tracks the ambient environment rather than being physiologically clamped. *This is my inference applied to the habitat, not a sourced claim about invertebrates as a whole* — and it has real exceptions (bumblebee and honeybee thermoregulation, regional endothermy in some large insects). Relevant supporting evidence that climate governs external host-associated microbiomes: Woodhams et al., *Nat Commun* / [PMC6996194](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6996194/) (654 host species, >15,000 samples; external microbiomes best explained by temperature range and precipitation seasonality, internal by host phylogeny/immune complexity and diet).
- **Distinctive surfaces and body fluids:** chitinous cuticle, calcium carbonate shell, mucus layers, hemolymph in an open circulatory system rather than a closed vascular bed. *Inference from general zoology; not sourced to a microbiome-specific study here.*
- **Taxonomic weight.** Invertebrates are >95% (some estimates 97%) of described animal species, against ~64,800 described chordates. Chapman, *Numbers of Living Species in Australia and the World*, 2nd ed., ABRS 2009 ([DCCEEW](https://www.dcceew.gov.au/science-research/abrs/publications/other/numbers-living-species)); 97% figure as used by Petersen & Osvatic 2018.

**Attested microbial content of the habitat** (evidence that this is a real, sampled, microbially distinctive place):

- **Sponges** — 81 species sampled globally; sponges are "a reservoir of exceptional microbial diversity and major contributors to the total microbial diversity of the world's oceans". Thomas et al., *Nat Commun* 7:11870 (2016), [doi:10.1038/ncomms11870](https://doi.org/10.1038/ncomms11870), PMC4912640.
- **Corals** — the coral holobiont: bacterial, archaeal, fungal, protistan and viral associates plus *Symbiodinium*. Bourne, Morrow & Webster, *Annu Rev Microbiol* 70:317–340 (2016), [doi:10.1146/annurev-micro-102215-095440](https://doi.org/10.1146/annurev-micro-102215-095440), PMID 27482741. Updated: Voolstra et al., *Nat Rev Microbiol* (2024), [doi:10.1038/s41579-024-01015-3](https://doi.org/10.1038/s41579-024-01015-3).
- **Nematodes** — the native gut microbiome of wild *Caenorhabditis*, distinct from the monoxenic lab condition. Dirksen et al., *BMC Biol* 14:38 (2016), [doi:10.1186/s12915-016-0258-1](https://doi.org/10.1186/s12915-016-0258-1), PMID 27160191.
- **BacDive's cultured isolates from this habitat** corroborate the breadth: *Teredinibacter turnerae* (shipworm), *Xenorhabdus* and *Photorhabdus* spp. (entomopathogenic nematode symbionts), *Endozoicomonas ascidiicola* (tunicate), *Sorangium cellulosum* and other myxobacteria, marine *Vibrio* spp. — see `data/raw/bacdive_source_taxa.tsv` under `bacdive.isolation_source:invertebrates-other`.

## 4. Sources

| Claim | Source |
|---|---|
| GOLD five-level classification; Host-associated categories are individual hosts or phyla; paths driven by curated samples | <https://gold.jgi.doe.gov/ecosystem_classification>; Mukherjee et al., *Nucleic Acids Res* 51(D1):D957–D963 (2023), [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974), PMID 36318257 (correction: [doi:10.1093/nar/gkae162](https://doi.org/10.1093/nar/gkae162)); GOLD v.10, [doi:10.1093/nar/gkae1000](https://doi.org/10.1093/nar/gkae1000) |
| `ENVO:01001002` definition, `ENVO:01001176` definition and placement, `ENVO:01001055`, `ENVO:01001179`, sparse child set | OLS4 API, ontology `envo`, retrieved 2026-08-17: <https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176>; ENVO papers [doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43), [doi:10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6) |
| No `Invertebrata` term in NCBITaxon / UBERON / BTO | OLS4 exact-label search, retrieved 2026-08-17 |
| Invertebrate = animal lacking a vertebral column | [Britannica](https://www.britannica.com/animal/invertebrate) |
| Invertebrata is paraphyletic, a grade not a clade | [Wikipedia, *Invertebrate*](https://en.wikipedia.org/wiki/Invertebrate); [Wikipedia, *Paraphyly*](https://en.wikipedia.org/wiki/Paraphyly) — tertiary; a curator wanting a citable source should use Brusca & Brusca, *Invertebrates*, 3rd ed. (Sinauer/OUP, 2016) |
| Invertebrates lack antibody-based adaptive immunity; innate recognition governs symbiosis | Nyholm & Graf 2012, [doi:10.1038/nrmicro2894](https://doi.org/10.1038/nrmicro2894) |
| Invertebrates = 97% of animal diversity, under-sampled in microbiome work, fewer associated microbes | Petersen & Osvatic 2018, [doi:10.1128/mSystems.00179-17](https://doi.org/10.1128/mSystems.00179-17) |
| >95% of described animal species; ~64,791 described chordates | Chapman 2009, ABRS, [DCCEEW](https://www.dcceew.gov.au/science-research/abrs/publications/other/numbers-living-species) |
| Sponge microbiome | Thomas et al. 2016, [doi:10.1038/ncomms11870](https://doi.org/10.1038/ncomms11870) |
| Coral holobiont | Bourne et al. 2016, [doi:10.1146/annurev-micro-102215-095440](https://doi.org/10.1146/annurev-micro-102215-095440); Voolstra et al. 2024, [doi:10.1038/s41579-024-01015-3](https://doi.org/10.1038/s41579-024-01015-3) |
| Nematode native microbiome | Dirksen et al. 2016, [doi:10.1186/s12915-016-0258-1](https://doi.org/10.1186/s12915-016-0258-1) |
| Host-associated metadata package, `host_taxid` | Yilmaz et al., *Nat Biotechnol* 29:415–420 (2011), [doi:10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823); MIxS-SA extension, *ISME Commun* (2022), [doi:10.1038/s43705-022-00092-w](https://doi.org/10.1038/s43705-022-00092-w) |
| GOLD node counts (621 at bare node; children Cnidaria/Nematoda/Echinodermata/Platyhelminthes/Bryozoans/Ctenophora/Tunicates; Arthropoda/Mollusca/Porifera/Annelida as siblings) | `data/raw/gold_ecosystem_paths.tsv`, this repo |

**Explicitly flagged as my inference, not sourced:** that 621 is a node-local rather than cumulative count; that ectothermy is a habitat-relevant property of essentially all invertebrate hosts; that cuticle/hemolymph/open circulation constitute a distinctive microbial setting; that GOLD's promotion of Arthropoda/Mollusca/Porifera to sibling categories is a sample-volume artefact rather than a semantic claim.

## 5. Synonyms and what not to conflate

**Names in real use for this concept**
- invertebrate-associated environment *(recommended primary label — matches the ENVO `X-associated environment` pattern and is the label already in `curation/term_requests.tsv`)*
- invertebrate host environment
- invertebrate-associated habitat
- invertebrate holobiont *(literature usage; strictly the host + microbes together, so an inexact synonym — avoid as an exact synonym)*
- GOLD: `Host-associated > Invertebrates`; BacDive: `Invertebrates-Other`

**Do not conflate with**

| Term | Why it is different |
|---|---|
| `ENVO:01001176` environment associated with an aquatic invertebrate | Narrower by an aquatic-habitat conjunct. Should become a **child** of the requested term, not a grounding target. |
| `ENVO:01001055` environment associated with an animal part or small animal | Parthood/size axis, includes vertebrate parts. |
| BacDive *host animal ectotherm* / *host animal endotherm* (`habitatmech:BACDIVE.e68bf42dcb`, `…3d543e6b49`) | Thermal-physiology axis. Fish, amphibians and reptiles are ectothermic **vertebrates**; the two categorisations cross-cut. |
| "Invertebrata" as a taxon | Not a clade and not a term in NCBITaxon. This concept is a *place determined by a host*, not a taxonomic grouping — the distinction this repo enforces after #114/#112. |
| Anatomical parts of an invertebrate — `gut`, `intestine`, `mucus`, `tissue`, `cocoon` | Per repo rule these ground to the anatomy term (`UBERON`/`ENVO`). Only the **whole organism as host** stays here. GOLD's `Host-associated > Invertebrates > Cnidaria > Coral > Mucus` and `> Tissue` are the part cases. |
| Benthic macroinvertebrates as a bioindicator assemblage | An ecological-assessment sampling target (the invertebrates are what is *counted*, not what is *sampled from*). Not this concept. |
| Coral reef biome, sponge ground, invertebrate burrow | Environments *containing* invertebrates, not environments *determined by* an invertebrate body. |
| BacDive `Invertebrates-Other` (`habitatmech:BACDIVE.e864a16f03`) | **Overlapping, not identical.** BacDive's is an explicit residual bucket ("Other"), so it is a subset by construction. It is, however, a strong candidate **co-attestor** if this record is defined to reading A — worth a curator decision either way, since it currently sits in `OTHER` category with no term of its own for exactly the same reason ("The invertebrate-associated environment terms in the slice are all aquatic-qualified"). |

## 6. Should it be a term at all?

**Yes.** This is a habitat, and it should be minted.

- It passes the repo's organism-as-habitat test: an organism acting as a host *is* a habitat, and ENVO models exactly this at plant-, animal- and fungi-associated environment. What is not a place is the taxon term — and here there is not even a taxon term to be confused with.
- It is not a disease, quality, process or procedure, so `NOT_APPLICABLE` would be wrong.
- It is directly sampled: 621 GOLD organisms are annotated at the bare node with no finer host, and BacDive attests 596 sources / 507 strains at its counterpart. Those are records of samples actually taken from an invertebrate whose identity was not resolved further — a real habitat description, not a placeholder.
- Nothing in ENVO, UBERON, FOODON, BTO or PO names it; the nearest term, `ENVO:01001176`, is narrower by an assertion the sources do not make. `CONFIRM_UNGROUNDED` + ENVO term request, as already recorded, is the right disposition.

**Two caveats a curator should carry onto the record:**

1. **It is a grade-level term, and the definition says so.** ENVO maintainers may object that a paraphyletic grouping is not a good basis for a class. The counter-argument to include in a term request is that ENVO already minted `ENVO:01001176` on exactly this differentia, and that the requested term is its natural, more general parent — accepting it tidies the hierarchy rather than complicating it. (The live `ENVO:01001176` definition also contains a typo, "vetebral", worth mentioning if a request is filed.)
2. **The GOLD-residual reading (§1, Reading B) is not the definition.** If the record is published with reading A, the fact that `Arthropoda`, `Mollusca`, `Porifera` and `Annelida` do not appear among its `parent_habitats` children is a fidelity-to-GOLD artefact and should be noted, so a downstream consumer does not read the absence as a claim that arthropods are not invertebrates.

**Sources:** [JGI GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification) · [GOLD v.9, NAR 2023](https://doi.org/10.1093/nar/gkac974) · [GOLD v.10, NAR 2025](https://doi.org/10.1093/nar/gkae1000) · [OLS4 ENVO:01001176](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176) · [ENVO 2013](https://doi.org/10.1186/2041-1480-4-43) · [ENVO 2016](https://doi.org/10.1186/s13326-016-0097-6) · [Nyholm & Graf 2012](https://doi.org/10.1038/nrmicro2894) · [Petersen & Osvatic 2018](https://doi.org/10.1128/mSystems.00179-17) · [Thomas et al. 2016](https://doi.org/10.1038/ncomms11870) · [Bourne et al. 2016](https://doi.org/10.1146/annurev-micro-102215-095440) · [Voolstra et al. 2024](https://doi.org/10.1038/s41579-024-01015-3) · [Dirksen et al. 2016](https://doi.org/10.1186/s12915-016-0258-1) · [Woodhams et al., PMC6996194](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6996194/) · [Marine invertebrate immunity 2024, PMC11359984](https://pmc.ncbi.nlm.nih.gov/articles/PMC11359984/) · [Chapman 2009, ABRS](https://www.dcceew.gov.au/science-research/abrs/publications/other/numbers-living-species) · [Yilmaz et al. 2011, MIxS](https://doi.org/10.1038/nbt.1823) · [MIxS-SA 2022](https://doi.org/10.1038/s43705-022-00092-w) · [Britannica, invertebrate](https://www.britannica.com/animal/invertebrate) · [Wikipedia, Invertebrate](https://en.wikipedia.org/wiki/Invertebrate) · [Wikipedia, Paraphyly](https://en.wikipedia.org/wiki/Paraphyly)

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. http://purl.obolibrary.org/obo/ENVO_01001002
3. https://doi.org/10.1186/2041-1480-4-43
4. https://doi.org/10.1186/s13326-016-0097-6
5. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO:01001176
6. https://www.britannica.com/animal/invertebrate
7. https://en.wikipedia.org/wiki/Invertebrate
8. https://en.wikipedia.org/wiki/Paraphyly
9. https://doi.org/10.1038/nrmicro2894
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC11359984/
11. https://doi.org/10.1128/mSystems.00179-17
12. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6996194/
13. https://www.dcceew.gov.au/science-research/abrs/publications/other/numbers-living-species
14. https://doi.org/10.1038/ncomms11870
15. https://doi.org/10.1146/annurev-micro-102215-095440
16. https://doi.org/10.1038/s41579-024-01015-3
17. https://doi.org/10.1186/s12915-016-0258-1
18. https://doi.org/10.1093/nar/gkac974
19. https://doi.org/10.1093/nar/gkae162
20. https://doi.org/10.1093/nar/gkae1000
21. https://doi.org/10.1038/nbt.1823
22. https://doi.org/10.1038/s43705-022-00092-w