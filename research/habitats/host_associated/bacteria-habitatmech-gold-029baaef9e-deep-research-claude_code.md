---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-17T14:51:48.283108'
end_time: '2026-08-17T15:01:35.333357'
duration_seconds: 587.05
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Bacteria
  habitat_identifier: habitatmech:GOLD.029baaef9e
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Microbial > Bacteria'
  assertions: '3017'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. GOLD''s
    Host-associated > Microbial > Bacteria: bacteria acting as host for another microbe.
    No environment term exists for a microbial host; ENVO''s organism-associated terms
    cover plants and animals only. ENVO term request. (source concept habitatmech:GOLD.029baaef9e)'
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
  web_search_requests: 21
  num_turns: 42
  total_cost_usd: 4.478038999999999
  session_id: cead077d-60b6-4a9c-85cb-c7dff5cba887
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 31
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Bacteria
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.029baaef9e
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Microbial > Bacteria
- **Upstream assertion volume:** 3017
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. GOLD's Host-associated > Microbial > Bacteria: bacteria acting as host for another microbe. No environment term exists for a microbial host; ENVO's organism-associated terms cover plants and animals only. ENVO term request. (source concept habitatmech:GOLD.029baaef9e)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Bacteria** as a microbial habitat, with citations.

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

# Definition research: *Bacteria* as a habitat — `habitatmech:GOLD.029baaef9e`

## Proposed definition

> **An environmental system determined by an organism which is determined by a living bacterium acting as host, comprising that bacterial cell's surface, envelope and interior insofar as they are colonised by other microorganisms.**

House-style (matches the phrasing of ENVO's existing siblings, if the curator prefers the terser form): *"An environmental system determined by a bacterium."* — this is the wording already staged in `curation/term_requests.tsv`. It parallels ENVO:01001001 / ENVO:01001002 / ENVO:01001041 exactly but carries no differentia beyond the host clade, which is defensible here precisely because the host clade *is* the whole content of the concept (see §3).

One caveat before the sections: the ideal parent is not `ENVO:01001000` but an intermediate *microbe-associated environment* (`habitatmech:GOLD.184623c963`, the GOLD parent `Host-associated > Microbial`), which does not exist in ENVO either and is requested in the same batch. Writing the definition against `ENVO:01001000` directly is a workaround for that missing intermediate class, not the correct final placement.

---

## 1. What the concept denotes

**The reading the data means.** The source path is `Host-associated > Microbial > Bacteria` — GOLD level 1 = Ecosystem (`Host-associated`), level 2 = Ecosystem Category (`Microbial`), level 3 = Ecosystem Type (`Bacteria`). In GOLD, level 1 `Host-associated` means the organism or sample was "collected … from another organism", and the Ecosystem Category for host-associated records is the host group ("individual hosts or phyla") ([GOLD Ecosystem Classification](https://gold.jgi.doe.gov/ecosystem_classification); Mukherjee et al., *Nucleic Acids Res* 51:D957–D963, 6 Jan 2023, [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974)). So the concept denotes **a bacterium in its role as host** — the physical place sampled is *another bacterium's cell*: its outer surface, its envelope/periplasm, or its cytoplasm. The thing a sample is taken from is the host bacterial cell (or a co-culture of host + resident).

**Internal evidence that this is the right reading, not a guess.** The only sibling elaborated under the same GOLD Ecosystem Category is `Host-associated > Microbial > Dinoflagellates > Endosymbionts` (`data/raw/gold_ecosystem_paths.tsv`). GOLD's `Microbial` category is therefore unambiguously "the host is a microbe", and its one elaborated Ecosystem Subtype is "endosymbionts of that host". `Bacteria` is the same construction with a bacterial host.

**What is inside the concept:** phages and other viruses replicating in a bacterial cell; epibiotic bacteria attached to a bacterial cell surface (Saccharibacteria/TM7, *Vampirococcus*, *Micavibrio*); periplasmic invaders (*Bdellovibrio*, in the bdelloplast); cytoplasmic residents (*Ca.* Moranella endobia inside *Ca.* Tremblaya princeps; *Daptobacter*).

**What is outside the concept (neighbouring concepts):** a biofilm or microbial mat — a multi-species aggregate, not one host cell (`ENVO:00002034`, `ENVO:01000008`); a bacterial culture as an engineered laboratory setting; and "a sample that happens to contain bacteria", which is every environmental sample in the corpus and is not what a `Host-associated` path asserts.

**Residual ambiguity — flagged, not resolved.** I could not determine *which* 3017 GOLD Organism records carry this path; `gold.jgi.doe.gov` returns HTTP 403 to automated fetches and no individual organism record surfaced in search. Two readings of the population are compatible with everything above, and they do not change the definition but do change what the record's attestation count means:

- **(a) phage/virus isolates classified by their bacterial host.** GOLD Organism entities explicitly include viruses, and IMG integrates phage genomes alongside host-associated ecosystem classifications ([GOLD Help](https://gold.jgi.doe.gov/help); Chen et al., IMG/M, *Nucleic Acids Res* 45:D507–D516, [doi:10.1093/nar/gkw929](https://doi.org/10.1093/nar/gkw929)). A count of ~3000 fits a phage-genome population far better than a symbiont one.
- **(b) bacterial symbionts, epibionts and predators of bacteria** — the *Dinoflagellates > Endosymbionts* sibling is the model for this.

My inference — and it is an inference, not a sourced claim — is that (a) dominates numerically and (b) is the conceptually central case. Either way the habitat denoted is the same: the host bacterial cell. Note `assertion_unit: ORGANISM` here; the 3017 are GOLD Organism records, not samples, and are not summable with BacDive or PREGO counts.

---

## 2. Genus — the broader kind

**Smallest well-established kind: an environmental system determined by a (host) organism.** The term exists: **`ENVO:01001000` — *environmental system determined by an organism*** — "An environmental system which is determined by a living organism", carrying the synonym **"host-associated environment"** and present in this repo's vendored slice (`data/raw/ontology_terms.tsv`; [OLS4](https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO%3A01001000)). The design pattern behind it — an environment named for the single entity whose removal would collapse the system — is documented in Buttigieg et al., *J Biomed Semantics* 4:43 (2013), [doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43) and 7:57 (2016), [doi:10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6).

`ENVO:01001000` is a *genus*, not a match: it is far broader than "bacterial host". Its direct children, verified via OLS4, are the near-misses:

| Candidate | Why it fails |
|---|---|
| `ENVO:01001001` plant-associated environment | Sibling, wrong host kingdom ("determined by a green plant") |
| `ENVO:01001002` animal-associated environment | Sibling, wrong host kingdom ("determined by an animal") |
| `ENVO:01001041` fungi-associated environment | Sibling, wrong host kingdom ("determined by a fungal structure") |
| `ENVO:2100000` anatomical entity environment | The other direct child. Its populated children are body-part environments of multicellular organisms. Whether a bacterial cell counts as an "anatomical entity" is arguable, but using this term would assert *part-of-an-organism*-hood and lose the host-organism reading entirely. Near-miss, and the closest thing to a trap. |
| `ENVO:00002034` biofilm / `ENVO:01000008` microbial mat | Both in the slice; both are multi-species aggregates or materials, not a single host cell. Narrower *and* asserting community structure the sources never claim. |
| `NCBITaxon:2` Bacteria | A taxon — a class of organisms, not a place. Per this repo's rule (#114) this is `relation: xref`, never grounding and never `parent`. |
| `GO:0043657` host cell | "A cell within a host organism. Includes the host plasma membrane and any external encapsulating structures such as the host cell wall and cell envelope." Genuinely close in *denotation*, but it is a GO cellular component used to locate a symbiont's gene products, not an environmental system, and it is not restricted to bacterial hosts. |
| `CL:0000520` prokaryotic cell | A cell type, not an environment. Not in the vendored slice. |

**Conclusion: nothing in ENVO expresses the concept, and nothing expresses its natural parent either.** ENVO's organism-determined branch resolves hosts at plant / animal / fungus and stops. This is not an oversight peculiar to ENVO — EMPO makes the identical cut, resolving host association at "host kingdom … Animal, Plant, or Fungus" ([EMPO](https://earthmicrobiome.org/protocols-and-standards/empo/); Thompson et al., *Nature* 551:457–463, 2017, [doi:10.1038/nature24621](https://doi.org/10.1038/nature24621)). ENVO issue [#1029](https://github.com/EnvironmentOntology/envo/issues/1029) (opened 20 Oct 2020, now closed) requested host-associated biome terms and likewise proposed only host/animal/human/plant variants; no microbial-host term was requested or added.

---

## 3. Differentia — what distinguishes it

The differentia is the **host clade: the determining organism is a bacterium** rather than a plant, animal or fungus. That is thin as differentiae go, but it is the same thin differentia ENVO already accepts across all three existing siblings, and it is the entire content of the source concept.

Three observable properties back it up and are what would separate it from its siblings in practice:

**(i) The host is unicellular, so the habitat is a single cell.** Unlike a plant- or animal-associated environment, there is no anatomy to descend into — the child terms are cell compartments, not organs. This is the structural reason the concept cannot be modelled by re-using `ENVO:2100000`.

**(ii) Three physically distinct microhabitats, each with a named occupancy mode.** Pérez et al.'s canonical scheme for bacteria-on-bacteria interaction is exactly a partition of the host cell as a place (*Environ Microbiol* 18:766–779, 2016, [doi:10.1111/1462-2920.13171](https://doi.org/10.1111/1462-2920.13171)):
- **cell surface (epibiotic)** — predator/symbiont attaches externally and never enters. *Vampirococcus lugosii* on *Halochromatium*; *Micavibrio*; *Bdellovibrio exovorus* on *Caulobacter*.
- **periplasm** — *Bdellovibrio bacteriovorus* enters the periplasm of Gram-negative prey and grows there within a rounded **bdelloplast** for ~3 h before lysis (`GO:0042597` periplasmic space: "the region between the inner (cytoplasmic) and outer membrane"). Sockett, *Annu Rev Microbiol* 63:523–539, 2009, [doi:10.1146/annurev.micro.091208.073346](https://doi.org/10.1146/annurev.micro.091208.073346); Caulton & Lovering, *Microbiology* 169:001380, 2023, [doi:10.1099/mic.0.001380](https://doi.org/10.1099/mic.0.001380).
- **cytoplasm** — *Ca.* Moranella endobia lives in the cytoplasm of *Ca.* Tremblaya princeps, many Moranella cells per Tremblaya cell. von Dohlen et al., *Nature* 412:433–436, 2001, [doi:10.1038/35086563](https://doi.org/10.1038/35086563); McCutcheon & von Dohlen, *Curr Biol* 21:1366–1372, 2011, [doi:10.1016/j.cub.2011.06.051](https://doi.org/10.1016/j.cub.2011.06.051); Husnik & McCutcheon, *PNAS* 113:E5416–E5424, 2016, [doi:10.1073/pnas.1603910113](https://doi.org/10.1073/pnas.1603910113).

  This axis is not just literature convention: MIxS-SA standardises it as a reportable field, `host_cellular_loc` (intracellular vs extracellular), alongside `host_taxid`, `type_of_symbiosis`, `host_dependence` and `host_of_host_taxid` — Jorge et al., *ISME Commun* 2:9, 2022, [doi:10.1038/s43705-022-00092-w](https://doi.org/10.1038/s43705-022-00092-w).

**(iii) The residents are obligately dependent and genomically reduced.** The bacterial cell is a resource-replete, biosynthetically complete environment, and its occupants converge on loss of biosynthesis: *Nanosynbacter lyticus* TM7x has a 705-kb genome with no amino-acid biosynthesis at all and is an obligate epibiont of *Schaalia* (*Actinomyces*) *odontolytica* XH001 (He et al., *PNAS* 112:244–249, 2015, [doi:10.1073/pnas.1419038112](https://doi.org/10.1073/pnas.1419038112)); *Vampirococcus lugosii* has a 1.31-Mbp genome reduced in biosynthetic metabolism (Moreira et al., *Nat Commun* 12:2454, 2021, [doi:10.1038/s41467-021-22762-4](https://doi.org/10.1038/s41467-021-22762-4)); *Ca.* Tremblaya princeps, itself a host, is at 139 kb. Castelle et al. generalise this for the CPR — small cells, small genomes, "often episymbiotic associations with other bacteria and archaea" (*Nat Rev Microbiol* 16:629–645, 2018, [doi:10.1038/s41579-018-0076-2](https://doi.org/10.1038/s41579-018-0076-2)). Note their hedge: *often*, not universally obligate — do not write "obligate" into the definition on Castelle's authority; He et al. 2015 is the source that supports obligacy, and only for TM7x.

**(iv) Scale.** If reading (a) in §1 is right, this is quantitatively the largest host-associated habitat class there is: phages are "the most abundant organisms in the biosphere", ~10³¹ particles, and every one of them requires a bacterial (or archaeal) cell to replicate in (Clokie et al., *Bacteriophage* 1:31–45, 2011, [doi:10.4161/bact.1.1.14942](https://doi.org/10.4161/bact.1.1.14942), PMID [21687533](https://pubmed.ncbi.nlm.nih.gov/21687533/)).

---

## 4. Sources

Standards and vocabularies
- GOLD Ecosystem Classification (five-level scheme; `Host-associated` = "collected … from another organism"): https://gold.jgi.doe.gov/ecosystem_classification (403 to automated fetch; content above is from GOLD's own indexed text and the GOLD papers)
- Mukherjee et al. 2023, GOLD v.9, *Nucleic Acids Res* 51:D957–D963 — [doi:10.1093/nar/gkac974](https://doi.org/10.1093/nar/gkac974) (PMID [36318257](https://pubmed.ncbi.nlm.nih.gov/36318257/))
- Mukherjee et al. 2025, GOLD v.10, *Nucleic Acids Res* 53:D989–D997 — [doi:10.1093/nar/gkae1000](https://doi.org/10.1093/nar/gkae1000)
- Ivanova et al. / GOLD five-level scheme origin, referenced from GOLD Help: https://gold.jgi.doe.gov/help
- Buttigieg et al. 2013, ENVO, *J Biomed Semantics* 4:43 — [doi:10.1186/2041-1480-4-43](https://doi.org/10.1186/2041-1480-4-43); Buttigieg et al. 2016, ENVO in 2016, 7:57 — [doi:10.1186/s13326-016-0097-6](https://doi.org/10.1186/s13326-016-0097-6)
- ENVO issue #1029, "EnvO terms for host-associated samples" (20 Oct 2020, closed) — https://github.com/EnvironmentOntology/envo/issues/1029
- Yilmaz et al. 2011, MIxS, *Nat Biotechnol* 29:415–420 — [doi:10.1038/nbt.1823](https://doi.org/10.1038/nbt.1823)
- Jorge et al. 2022, MIxS-SA symbiont-associated extension, *ISME Commun* 2:9 — [doi:10.1038/s43705-022-00092-w](https://doi.org/10.1038/s43705-022-00092-w) (PMC [9723553](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9723553/))
- EMPO — https://earthmicrobiome.org/protocols-and-standards/empo/ ; Thompson et al. 2017, *Nature* 551:457–463 — [doi:10.1038/nature24621](https://doi.org/10.1038/nature24621)
- Term records verified against `data/raw/ontology_terms.tsv` and OLS4: `ENVO:01001000`, `ENVO:01001001`, `ENVO:01001002`, `ENVO:01001041`, `ENVO:2100000`, `ENVO:00002034`, `ENVO:01000008`, `NCBITaxon:2`, `GO:0043657`, `GO:0042597`, `CL:0000520`

Primary literature
- He et al. 2015, TM7x epibiotic parasitism, *PNAS* 112:244–249 — [doi:10.1073/pnas.1419038112](https://doi.org/10.1073/pnas.1419038112)
- Moreira et al. 2021, *Vampirococcus lugosii*, *Nat Commun* 12:2454 — [doi:10.1038/s41467-021-22762-4](https://doi.org/10.1038/s41467-021-22762-4) (PMID [33911080](https://pubmed.ncbi.nlm.nih.gov/33911080/))
- Sockett 2009, *Annu Rev Microbiol* 63:523–539 — [doi:10.1146/annurev.micro.091208.073346](https://doi.org/10.1146/annurev.micro.091208.073346)
- Caulton & Lovering 2023, *Microbiology* 169:001380 — [doi:10.1099/mic.0.001380](https://doi.org/10.1099/mic.0.001380) (PMC [10482364](https://pmc.ncbi.nlm.nih.gov/articles/PMC10482364/))
- Lai, Ford & Huwiler 2023, *Front Microbiol* 14:1168709 — [doi:10.3389/fmicb.2023.1168709](https://doi.org/10.3389/fmicb.2023.1168709)
- Pérez et al. 2016, "Bacterial predation: 75 years and counting!", *Environ Microbiol* 18:766–779 — [doi:10.1111/1462-2920.13171](https://doi.org/10.1111/1462-2920.13171)
- von Dohlen et al. 2001, *Nature* 412:433–436 — [doi:10.1038/35086563](https://doi.org/10.1038/35086563)
- McCutcheon & von Dohlen 2011, *Curr Biol* 21:1366–1372 — [doi:10.1016/j.cub.2011.06.051](https://doi.org/10.1016/j.cub.2011.06.051)
- Husnik & McCutcheon 2016, *PNAS* 113:E5416–E5424 — [doi:10.1073/pnas.1603910113](https://doi.org/10.1073/pnas.1603910113)
- Castelle et al. 2018, CPR/DPANN, *Nat Rev Microbiol* 16:629–645 — [doi:10.1038/s41579-018-0076-2](https://doi.org/10.1038/s41579-018-0076-2)
- Clokie et al. 2011, "Phages in nature", *Bacteriophage* 1:31–45 — [doi:10.4161/bact.1.1.14942](https://doi.org/10.4161/bact.1.1.14942)
- Varon & Levisohn 1972, three-membered parasitic system (phage → *Bdellovibrio* → *E. coli*), *Antimicrob Agents Chemother* 2:356–363 — PMID [4670503](https://pubmed.ncbi.nlm.nih.gov/4670503/)

**Explicitly my inference, not a source's claim:** (1) that the 3017 GOLD Organism records under this path are predominantly phage genomes; (2) that `ENVO:2100000` is a poor fit because a bacterial cell is not the kind of anatomical entity ENVO populates it with — ENVO states no such exclusion; (3) that the concept's natural parent is a *microbe-associated environment* class, which is a modelling proposal, not an existing standard.

---

## 5. Synonyms, and what not to conflate

**Names in real use for the concept**
- bacterium-associated environment (the requested term label)
- bacterial host cell / host bacterium / **basibiont** (the term used for the host in the TM7x–*Actinomyces* literature)
- prey cell (predation literature); **bdelloplast** for the specific periplasm-occupied state
- host cell environment; intrabacterial environment (for the cytoplasmic case)

**Commonly but wrongly treated as the same thing**
- **`NCBITaxon:2` Bacteria, the taxon.** The single most likely error. The taxon is a class of organisms; the habitat is a bacterium acting as host. Per #114, the taxon goes in `relation: xref`, the concept keeps its own identity, and `NOT_APPLICABLE` is *not* the right disposition.
- **"Bacterial" as a description of a sample's contents.** "Bacteria were found in this soil" is not a host-associated habitat. GOLD's level-1 `Host-associated` is what excludes this reading.
- **Biofilm (`ENVO:00002034`) / microbial mat (`ENVO:01000008`).** Multi-species aggregates. A biofilm contains bacteria; it is not one bacterium hosting another. Note the interaction runs the other way too: TM7x modulates its host's susceptibility to phage within biofilms (Zhong et al., *PNAS* 121:e2319790121, 2024, [doi:10.1073/pnas.2319790121](https://doi.org/10.1073/pnas.2319790121)) — but the biofilm is the surrounding setting, not this concept.
- **"Microbial" as a synonym for the parent.** The GOLD parent `Host-associated > Microbial` (`habitatmech:GOLD.184623c963`) covers dinoflagellate and other microbial hosts too; `Bacteria` is strictly narrower.
- **Human/animal microbiome habitats.** A bacterium in a gut is animal-associated, not bacterium-associated. The distinction is *whose cell is the place*.
- **Bacterial culture medium or a laboratory co-culture.** Engineered setting, not the host cell.

---

## 6. Should it be a term at all?

**Yes.** This is a habitat, and it is the case the repo's own rule was written for: *"An organism acting as a host IS a habitat; the taxon term is not"* (CLAUDE.md, #114). A bacterium hosting a phage, an epibiont or an endosymbiont is where the resident microbe lives — the same relation ENVO already models at plant-, animal- and fungi-associated environment. It is not a process, a quality, a disease state or a sampling artefact, so `NOT_APPLICABLE` would be the wrong and stronger claim.

Two dispositions follow, and they should not be collapsed:
1. **Keep the minted identity, ground nothing.** `UNGROUNDED` is correct: `ENVO:01001000` is a genus, not the concept, and grounding to it would merge every microbial host clade onto one record.
2. **`NCBITaxon:2` as `relation: xref`, never `parent`.** *Bacteria* the taxon is not broader than *an environment determined by a bacterium*; it is a different kind of thing.

**One structural warning for the term request.** The record currently has no `parent_habitats` entry pointing at an ontology term and, per `curation/term_requests/needs_a_parent_first.tsv`, that is exactly why it stalled. The clean submission is a **pair**: request *microbe-associated environment* (child of `ENVO:01001000`) and *bacterium-associated environment* (child of the former) together, and say so in the request, rather than parenting the bacterial term directly to the organism root and asking editors to re-parent it later. If ENVO editors decline the intermediate class, `ENVO:01001000` as direct parent is the fallback and the definition above still holds.

*Note: per the standing rule, this is research material only — no ENVO submission should be made without your explicit yes for this specific request.*

## Citations

1. https://gold.jgi.doe.gov/ecosystem_classification
2. https://doi.org/10.1093/nar/gkac974
3. https://gold.jgi.doe.gov/help
4. https://doi.org/10.1093/nar/gkw929
5. https://www.ebi.ac.uk/ols4/ontologies/envo/classes?obo_id=ENVO%3A01001000
6. https://doi.org/10.1186/2041-1480-4-43
7. https://doi.org/10.1186/s13326-016-0097-6
8. https://earthmicrobiome.org/protocols-and-standards/empo/
9. https://doi.org/10.1038/nature24621
10. https://github.com/EnvironmentOntology/envo/issues/1029
11. https://doi.org/10.1111/1462-2920.13171
12. https://doi.org/10.1146/annurev.micro.091208.073346
13. https://doi.org/10.1099/mic.0.001380
14. https://doi.org/10.1038/35086563
15. https://doi.org/10.1016/j.cub.2011.06.051
16. https://doi.org/10.1073/pnas.1603910113
17. https://doi.org/10.1038/s43705-022-00092-w
18. https://doi.org/10.1073/pnas.1419038112
19. https://doi.org/10.1038/s41467-021-22762-4
20. https://doi.org/10.1038/s41579-018-0076-2
21. https://doi.org/10.4161/bact.1.1.14942
22. https://pubmed.ncbi.nlm.nih.gov/21687533/
23. https://pubmed.ncbi.nlm.nih.gov/36318257/
24. https://doi.org/10.1093/nar/gkae1000
25. https://doi.org/10.1038/nbt.1823
26. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9723553/
27. https://pubmed.ncbi.nlm.nih.gov/33911080/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC10482364/
29. https://doi.org/10.3389/fmicb.2023.1168709
30. https://pubmed.ncbi.nlm.nih.gov/4670503/
31. https://doi.org/10.1073/pnas.2319790121