---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-17T20:38:18.328067'
end_time: '2026-08-17T20:44:03.198776'
duration_seconds: 344.87
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Cnidaria
  habitat_identifier: habitatmech:GOLD.e3fede2aea
  habitat_category: HOST_ASSOCIATED
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Host-associated > Cnidaria'
  assertions: '95'
  parent_terms: ENVO:01001000
  xrefs: mesh:D003063
  decision_note: "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest\
    \ broader term mesh:D003063 'Cnidaria' attached as a parent. Host-taxon reversal\
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
    \ not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.e3fede2aea)"
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
  web_search_requests: 8
  num_turns: 23
  total_cost_usd: 2.067043
  session_id: e7aeb369-65b1-40ca-b8c4-0672d5e7c9a9
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 26
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Cnidaria
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.e3fede2aea
- **Category:** HOST_ASSOCIATED
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Host-associated > Cnidaria
- **Upstream assertion volume:** 95
- **Nearest broader term already on the record:** ENVO:01001000
- **Cross-references upstream suggested:** mesh:D003063

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term mesh:D003063 'Cnidaria' attached as a parent. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it — the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM — a phylum is a class of organisms, not a place — so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.e3fede2aea)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Cnidaria** as a microbial habitat, with citations.

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

# Cnidaria (habitatmech:GOLD.e3fede2aea) — novel-term research

> **A cnidarian-associated environment which is determined by any cnidarian, at any life stage, considered as a whole organism rather than by a single anatomical part of one.**

**Headline finding: this concept should not get a minted HabitatMech definition, because ENVO already has the term.** `ENVO:01001179` *cnidarian-associated environment* — "An environmental system determined by a cnidarian or part of a cnidarian" — is a live, non-obsolete, defining-ontology ENVO class, a direct `rdfs:subClassOf` of `ENVO:01001002` *animal-associated environment*, and it is **already present in this repo's vendored slice** (`data/raw/ontology_terms.tsv`, `deprecated` blank, `directly_referenced=TRUE`). The recorded decision — "Confirmed UNGROUNDED: no ontology term fits this concept" — is factually wrong, and the corpus contradicts it in its own files. The recommended action is a `GROUND` to `ENVO:01001179`, not a term request. Details in §6.

---

## 0. The contradiction inside the corpus

This matters more than any literature finding, so it goes first. Two days before the UNGROUNDED decision was recorded, the sibling record `data/habitats/host_associated/coral.yaml` (`habitatmech:GOLD.a12eda25e9`) was curated `GROUND_AS_PARENT` → `ENVO:01001179` with this note:

> "Kept as a narrower kind of cnidarian-associated environment rather than grounded to it, **because Host-associated > Cnidaria is the shallower path entitled to that term**."

`Host-associated > Cnidaria` *is* `habitatmech:GOLD.e3fede2aea` — the concept in this brief. The Coral curation deliberately withheld the term so this record could claim it, and then this record was marked UNGROUNDED on the ground that the term does not exist. Both `curation/decisions.tsv:1557` (Coral, `GROUND_AS_PARENT ENVO:01001179`) and `curation/decisions.tsv:1609` (this concept, `CONFIRM_UNGROUNDED mesh:D003063`) are in the tree today.

The GOLD path table shows two paths ending in "Cnidaria":

| canonical_path | depth | identifier | current decision |
|---|---|---|---|
| `Host-associated > Cnidaria` | 2 | `GOLD.e3fede2aea` | CONFIRM_UNGROUNDED |
| `Host-associated > Invertebrates > Cnidaria` | 3 | `GOLD.00086e0958` | CONFIRM_UNGROUNDED |

Under the repo's shallowest-claims-the-term rule for ambiguous GOLD leaves, the depth-2 path (this concept) is the one entitled to `ENVO:01001179`; the depth-3 path takes `GROUND_AS_PARENT` / `NARROW`, as Coral did. That is a separate decision row, but it falls out of the same finding.

---

## 1. What the concept denotes

**The physical thing sampled:** the body of a cnidarian animal — its tissues, its secreted surface mucus, its gastrovascular cavity contents, and (in calcifying taxa) its skeleton — taken as the environment in which the microorganisms live. GOLD's `assertion_unit` here is `ORGANISM` (95 assertions), i.e. 95 sequenced organisms whose recorded isolation environment was "a cnidarian", with no further specification of taxon or body part.

Cnidaria is an accepted phylum (Hatschek, 1888) comprising the subphyla Anthozoa, Medusozoa and Endocnidozoa ([WoRMS AphiaID 1267](https://www.marinespecies.org/aphia.php?p=taxdetails&id=1267)) — so the concept spans hard corals, soft corals and gorgonians, sea anemones, hydroids and *Hydra*, and jellyfish, plus the parasitic myxozoans.

**What is inside the boundary.** Any microbial sample whose immediate environment is a cnidarian body or its secretions, with the host identified no more precisely than the phylum, or identified as a cnidarian that is not a coral. In GOLD's own tree the children of this node are `Coral`, and below that `Tissue`, `Mucus`, `Surface`.

**What is outside — the boundary a curator must state explicitly.**

- **The reef is not the host.** `ENVO:00000150` *coral reef*, `ENVO:01000049` *marine coral reef biome*, `ENVO:01000143` *marine reef* are geographic/biome features built partly of dead coral skeleton and surrounding seawater. A reef-water or reef-sediment sample is not a cnidarian-associated environment. This is the single most common conflation for this concept.
- **The taxon is not the place.** `mesh:D003063` *Cnidaria* and NCBITaxon:6073 denote a class of organisms. Per repo policy (#99, #114) these stay `relation: xref`; they are not parents.
- **Neighbouring host-associated concepts:** Porifera/sponge, Mollusca, Echinodermata, and the annelid/arthropod host records are sibling concepts under the same genus, not sub- or super-classes of this one.
- **The dinoflagellate symbiont is a resident, not the habitat.** Symbiodiniaceae are part of the holobiont being sampled, not the enclosing environment. (MIxS handles the nested case explicitly through the symbiont-associated extension — see §4.)

**Ambiguity assessment.** The label "Cnidaria" is ambiguous in the abstract between (a) the taxon and (b) the host environment, and this ambiguity is exactly what #114 was about. The source path settles it: GOLD files it under `Host-associated`, whose semantics are "the environment from which the organism was obtained is a host". Reading (b) is what the data means. There is no residual ambiguity about *which* cnidarians — the phylum is the intended scope, and the more specific corals are a separate, deeper GOLD node.

---

## 2. Genus — the broader kind

**Genus: `ENVO:01001002` *animal-associated environment*** — "An environmental system determined by an animal." This is the direct asserted parent of `ENVO:01001179` in ENVO ([OLS4 hierarchicalParents](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179/hierarchicalParents)), and is itself a subclass of `ENVO:01001000` *environmental system determined by an organism* — the term currently sitting on this record as `parent_habitats`.

**The existing term that expresses the concept itself, not just its genus:**

| CURIE | Label | Definition | Status |
|---|---|---|---|
| `ENVO:01001179` | cnidarian-associated environment | An environmental system determined by a cnidarian or part of a cnidarian. | Not obsolete; subset `envoMeo`; no synonyms; no dbxrefs; in this repo's vendored slice |

Verified live at [OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179) and in `data/raw/ontology_terms.tsv`, so a `GROUND` will pass the seeder's slice-membership and label check.

**Near-misses recorded, and why each fails.**

- `ENVO:01001176` *environment associated with an aquatic invertebrate* — "An environment shaped by a vertebrate-lacking metazoan inhabiting aquatic systems." Broader than the concept (covers sponges, molluscs, echinoderms), and it also asserts *aquatic*, which is true of essentially all cnidarians but is an extra claim the GOLD path does not make. Not the identity; would be a defensible additional parent, but `ENVO:01001179` makes it unnecessary.
- `ENVO:01001055` *environment associated with an animal part or small animal* — narrower and differently framed (part-level or small-bodied); a jellyfish is neither.
- `ENVO:00000150` *coral reef*, `ENVO:01000049` *marine coral reef biome*, `ENVO:01000029` *marine reef biome* — these are biome/geographic-feature classes, not host-associated environments. Grounding here would relocate the sample from the animal to the seascape. Note also that `ENVO:00000150` is flagged `deprecated=TRUE` in the vendored slice.
- `BTO:0006350` *polyp* / `BTO:0006391` *ephyra* / `BTO:0006151` *coral nubbin* — life-stage or experimental-preparation terms, all narrower than the phylum; `BTO:0006350` is deprecated. A nubbin is a laboratory artefact, not a habitat class.
- `mesh:D003063` *Cnidaria* — the taxon. Correct as an `xref`, wrong as a parent (#99).

---

## 3. Differentia — what distinguishes it from its siblings

The differentia that separates this from the other `animal-associated environment` children is simply **the identity of the determining host: an animal of the phylum Cnidaria**. That is the whole of it, and it is the form ENVO uses for every sibling in this branch. Everything below is *supporting* evidence a curator can cite for why cnidarians are a coherent and distinctive microbial habitat — it is context for the term request/grounding rationale, not additional clauses for the one-sentence definition.

**Observable properties that make the class biologically non-arbitrary:**

1. **Compartmentalised, physicochemically distinct micro-habitats within one body.** The cnidarian host provides tissue, gastrovascular cavity, skeleton, and surface mucus layer, each with a distinct microbial community ([Apprill et al. 2016, *mSystems* 1:e00143-16](https://journals.asm.org/doi/10.1128/msystems.00143-16)). This is directly mirrored in GOLD's own children of the Coral node (`Tissue`, `Mucus`, `Surface`).
2. **The surface mucus layer as a defining interface.** A gel of sulphated glycoprotein polymers, polysaccharides and lipids, secreted by mucocytes from photosynthate supplied by the endosymbiotic dinoflagellates; it traps particulates, carries higher organic-matter and nutrient concentrations than seawater, and hosts a microbiota with almost no overlap with the adjacent water column ([Glasl, Herndl & Frade 2016, *ISME J* 10:2280–2292](https://www.nature.com/articles/ismej20169)). Bacterial abundance in coral mucus is roughly 3–6× that of surrounding seawater by direct count ([Garren & Azam 2010, *AEM* 76:6128–6133](https://journals.asm.org/doi/10.1128/aem.01100-10)) — note that the widely repeated "order of magnitude" figure is *not* what that paper measured.
3. **Endolithic skeletal habitat unique to the calcifying members.** The skeleton harbours a species-rich community — the green alga *Ostreobium*, fungi, prokaryotes — with steep microbially generated physicochemical gradients producing fine-scale micro-niches ([Ricci et al. 2019, *Microbiome* 7:159](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-019-0762-y)).
4. **Host-specific, vertically persistent bacterial partners across the phylum, not just in corals.** Species-specific microbiota are maintained long-term in *Hydra*; *Nematostella vectensis* shows body-region-specific communities (spirochaete-dominated capitulum vs. proteobacteria-dominated mesenteries and physa) and genotype × environment structuring ([Baldassarre et al. 2023, *ISME J*/PMC9894556](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9894556/)); *Aurelia aurita* differs between exumbrella and gastral cavity and across benthic vs. planktonic life stages, and removing the native microbiome alters survival, growth and reproduction ([Weiland-Bräuer et al. 2020, *mBio*](https://pubmed.ncbi.nlm.nih.gov/32127452/)). Core coral bacterial phylotypes are shared across species thousands of kilometres apart ([Ainsworth et al. 2015, *ISME J* 9:2261–2274](https://www.nature.com/articles/ismej201539)); *Endozoicomonas* can exceed 90% of the bacterial community in some corals and localises to intracellular aggregates in tissue rather than mucus ([Neave et al. 2017; Pogoreutz et al., Trends Microbiol. 2023](https://www.cell.com/trends/microbiology/abstract/S0966-842X(23)00323-2)).
5. **The holobiont framing is the standard unit of analysis for this phylum.** The coral holobiont — cnidarian host plus bacteria, archaea, viruses, dinoflagellate and other eukaryotic microbes — is the organising concept of the field ([Rohwer et al. 2002, *MEPS* 243:1–10](https://www.int-res.com/abstracts/meps/v243/p1-10/); reviewed in [Voolstra et al. 2024, *Nat Rev Microbiol* 22:460–475](https://www.nature.com/articles/s41579-024-01015-3), [PMID 38438489](https://pubmed.ncbi.nlm.nih.gov/38438489/)).

**Explicit inference flags.** Points 1–5 are sourced. The claim that these properties *justify a phylum-level habitat class* rather than a coral-level one is my inference, and it is a weak one — most of the compartment literature is coral-specific, and the anemone/jellyfish/*Hydra* evidence supports host-specificity but not a shared phylum-wide physicochemistry. A curator should not write a definition asserting phylum-wide mucus or skeleton properties. ENVO's actual definition wisely asserts none of this: it names only the determining organism.

---

## 4. Sources

**Ontology and standards**

- ENVO:01001179 *cnidarian-associated environment* — [OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179) · [purl](http://purl.obolibrary.org/obo/ENVO_01001179). Not obsolete; parent `ENVO:01001002`; subset `envoMeo`.
- ENVO:01001002 *animal-associated environment*; ENVO:01001000 *environmental system determined by an organism*; ENVO:01001176 *environment associated with an aquatic invertebrate* (dbxref `MEO_0000871`) — all via [OLS4 ENVO](https://www.ebi.ac.uk/ols4/ontologies/envo).
- ENVO/MIxS usage guidance for host-associated samples: [EnvO wiki, "Using ENVO with MIxS"](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS); open discussion of host-associated biome terms, [EnvO issue #1029](https://github.com/EnvironmentOntology/envo/issues/1029).
- `env_medium` [MIXS:0000014] definition and ENVO-triad serialisation: [NMDC schema docs](https://microbiomedata.github.io/nmdc-schema/env_medium/).
- MIxS-SA symbiont-associated extension (directly relevant to coral–Symbiodiniaceae nesting): Holmes et al. 2022, *ISME Communications* 2:9 — [doi:10.1038/s43705-022-00092-w](https://www.nature.com/articles/s43705-022-00092-w) · [PMC9723553](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9723553/).
- WoRMS Cnidaria (phylum, Hatschek 1888; Anthozoa / Medusozoa / Endocnidozoa) — [AphiaID 1267](https://www.marinespecies.org/aphia.php?p=taxdetails&id=1267).
- MeSH D003063 *Cnidaria* — [meshb.nlm.nih.gov/record/ui?ui=D003063](https://meshb.nlm.nih.gov/record/ui?ui=D003063).

**Primary and review literature**

- Voolstra CR et al. (2024) The coral microbiome in sickness, in health and in a changing world. *Nature Reviews Microbiology* 22:460–475. [doi:10.1038/s41579-024-01015-3](https://www.nature.com/articles/s41579-024-01015-3) · PMID [38438489](https://pubmed.ncbi.nlm.nih.gov/38438489/)
- Apprill A et al. (2016) Distinguishing between microbial habitats unravels ecological complexity in coral microbiomes. *mSystems* 1:e00143-16. [doi:10.1128/msystems.00143-16](https://journals.asm.org/doi/10.1128/msystems.00143-16) · [PMC5080407](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5080407/)
- Glasl B, Herndl GJ, Frade PR (2016) The microbiome of coral surface mucus has a key role in mediating holobiont health and survival upon disturbance. *ISME J* 10:2280–2292. [doi:10.1038/ismej.2016.9](https://www.nature.com/articles/ismej20169) · [PMC4989324](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4989324/)
- Ricci F et al. (2019) Beneath the surface: community assembly and functions of the coral skeleton microbiome. *Microbiome* 7:159. [doi:10.1186/s40168-019-0762-y](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-019-0762-y) · PMID [31831078](https://pubmed.ncbi.nlm.nih.gov/31831078/)
- Ainsworth TD et al. (2015) The coral core microbiome identifies rare bacterial taxa as ubiquitous endosymbionts. *ISME J* 9:2261–2274. [doi:10.1038/ismej.2015.39](https://www.nature.com/articles/ismej201539)
- Rohwer F, Seguritan V, Azam F, Knowlton N (2002) Diversity and distribution of coral-associated bacteria. *Mar Ecol Prog Ser* 243:1–10. [doi:10.3354/meps243001](https://www.int-res.com/abstracts/meps/v243/p1-10/)
- Garren M, Azam F (2010) New method for counting bacteria associated with coral mucus. *Appl Environ Microbiol* 76:6128–6133. [doi:10.1128/AEM.01100-10](https://journals.asm.org/doi/10.1128/aem.01100-10)
- Baldassarre L et al. (2023) Genotype–environment interactions determine microbiota plasticity in the sea anemone *Nematostella vectensis*. [PMC9894556](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9894556/)
- Weiland-Bräuer N et al. (2020) Native microbiome depletion in *Aurelia aurita* alters fitness and pathogen resistance. *mBio*. PMID [32127452](https://pubmed.ncbi.nlm.nih.gov/32127452/)
- Pogoreutz C, Ziegler M et al. (2023) Frenemies on the reef? Resolving the coral–*Endozoicomonas* association. *Trends Microbiol*. [doi:10.1016/j.tim.2023.11.006](https://www.cell.com/trends/microbiology/abstract/S0966-842X(23)00323-2)
- van Oppen MJH, Blackall LL et al. (2023) The coral microbiome: molecular mechanisms of coral–microbiota interactions. *FEMS Microbiol Rev* 47:fuad005. [doi:10.1093/femsre/fuad005](https://academic.oup.com/femsre/article/47/2/fuad005/7071893)

**Repo-internal evidence** (verifiable, not literature): `data/raw/ontology_terms.tsv` (ENVO:01001179 present, not deprecated); `data/raw/ontology_subclass_edges.tsv` (`ENVO:01001179 rdfs:subClassOf ENVO:01001002`); `data/raw/gold_ecosystem_paths.tsv` (six Cnidaria paths, depths 2–5); `curation/decisions.tsv:1557,1608,1609`; `data/habitats/host_associated/coral.yaml`.

---

## 5. Synonyms, and what not to conflate

**Names in real use for this concept**

- cnidarian-associated environment (ENVO's label)
- cnidarian host environment / cnidarian-associated habitat
- cnidarian holobiont (used in the literature for host + microbiota as a unit; a *close* but not exact synonym — the holobiont includes the microbes, whereas the habitat concept is the host as an environment. Recommend recording as a related term, not an exact synonym.)
- coelenterate-associated environment (from the older, now-abandoned grouping "Coelenterata", which also swept in ctenophores — historically attested, taxonomically wrong; do not add as a synonym without that caveat)

**Do not conflate with**

| Not the same thing | Why |
|---|---|
| coral reef / marine coral reef biome (`ENVO:00000150`, `ENVO:01000049`) | A geographic/biome feature made largely of dead skeleton plus water and sediment; the living animal is a different environment. Communities in reef water show almost no overlap with mucus communities (Glasl et al. 2016). |
| the taxon *Cnidaria* (`mesh:D003063`, NCBITaxon:6073) | A class of organisms, not a place. `relation: xref` per #99. |
| Coral (`habitatmech:GOLD.a12eda25e9`) | A proper subset — anthozoan calcifiers only, already curated NARROW under this term. |
| Porifera / sponge-associated environments | Sibling host phylum, frequently lumped with corals as "reef invertebrates" in sampling metadata. |
| Symbiodiniaceae / zooxanthellae | Resident symbionts inside the habitat, not the habitat. MIxS-SA exists precisely to keep the nesting straight. |
| coral nubbin (`BTO:0006151`) | A laboratory preparation (fragments glued to substrate in flow-through tanks), i.e. a sampling/culturing artefact, not an environmental class. |
| Ctenophora (comb jellies) | Separate phylum; only conflated through the obsolete "Coelenterata". |

---

## 6. Should this be a term at all?

**No — it should be grounded, not minted.** The concept is unambiguously a habitat (an organism acting as a host is where the microbe lives; §1), so `NOT_APPLICABLE` was indeed the wrong disposition and the #114 reversal was correct in direction. But the reversal overshot: it moved the record from `NOT_APPLICABLE` to `CONFIRM_UNGROUNDED` + term-request candidate, when the term it would be requesting **already exists in ENVO and is already in this repo's vendored slice**. Filing an ENVO term request for *cnidarian-associated environment* would be requesting a duplicate of `ENVO:01001179`.

Recommended decision row for `habitatmech:GOLD.e3fede2aea`:

```
GROUND   ENVO:01001179   cnidarian-associated environment   (exact)
xrefs:   mesh:D003063 (taxon — xref only, per #99)
```

This clears the seeder's slice-membership and label-match gate (the term and its exact label are both in `data/raw/ontology_terms.tsv`), and it makes `coral.yaml`'s existing NARROW parenting coherent: Coral becomes a narrower kind of a term this record now *is*, which is what the Coral note said should happen.

Two consequential follow-ons a curator should handle in the same pass, both flagged rather than assumed:

1. **`habitatmech:GOLD.00086e0958`** (`Host-associated > Invertebrates > Cnidaria`, depth 3) carries the identical CONFIRM_UNGROUNDED note. Under the shallowest-claims-the-term convention it should become `GROUND_AS_PARENT` / `NARROW` on `ENVO:01001179`, matching Coral's treatment — not UNGROUNDED.
2. **Scope of the #114 sweep.** The same boilerplate note ("no ontology term fits this concept") appears on this record, on GOLD.00086e0958, and — judging by the untracked research files in the working tree — across a large cohort of host-taxon records. At least one member of that cohort had an exact ENVO term available and in-slice. That is worth an issue in its own right: the sweep asserted a negative ("no ontology term fits") without re-running the ontology lookup, and for this concept the negative is false.

## Citations

1. https://www.marinespecies.org/aphia.php?p=taxdetails&id=1267
2. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179/hierarchicalParents
3. https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179
4. https://journals.asm.org/doi/10.1128/msystems.00143-16
5. https://www.nature.com/articles/ismej20169
6. https://journals.asm.org/doi/10.1128/aem.01100-10
7. https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-019-0762-y
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9894556/
9. https://pubmed.ncbi.nlm.nih.gov/32127452/
10. https://www.nature.com/articles/ismej201539
11. https://www.cell.com/trends/microbiology/abstract/S0966-842X(23
12. https://www.int-res.com/abstracts/meps/v243/p1-10/
13. https://www.nature.com/articles/s41579-024-01015-3
14. https://pubmed.ncbi.nlm.nih.gov/38438489/
15. http://purl.obolibrary.org/obo/ENVO_01001179
16. https://www.ebi.ac.uk/ols4/ontologies/envo
17. https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
18. https://github.com/EnvironmentOntology/envo/issues/1029
19. https://microbiomedata.github.io/nmdc-schema/env_medium/
20. https://www.nature.com/articles/s43705-022-00092-w
21. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9723553/
22. https://meshb.nlm.nih.gov/record/ui?ui=D003063
23. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5080407/
24. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4989324/
25. https://pubmed.ncbi.nlm.nih.gov/31831078/
26. https://academic.oup.com/femsre/article/47/2/fuad005/7071893