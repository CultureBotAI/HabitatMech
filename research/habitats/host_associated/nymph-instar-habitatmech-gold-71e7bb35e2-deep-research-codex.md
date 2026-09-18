> An animal-associated environment which is determined by an immature insect in a post-embryonic nymphal instar before the adult molt.

**What It Denotes**

`Nymph/Instar`, in GOLD's `Host-associated > Arthropoda: Insects > Nymph/Instar` path, denotes the nymph-stage insect host as the microbial habitat: the body of a hemimetabolous insect sampled before it becomes a reproductive adult. That body-level habitat can include the cuticle, gut, hemolymph, fat body, bacteriomes, reproductive primordia, and other host tissues if the sample is an undissected nymph or homogenate.

The boundary follows the GOLD tree in [gold_ecosystem_paths.tsv](/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/data/raw/gold_ecosystem_paths.tsv): `Nymph/Instar > Gut`, `Nymph/Instar > Gut > Fecal`, and `Nymph/Instar > Whole body` are child/refinement concepts under this one, while `Larva`, `Prepupa`, `Pupa`, `Ootheca/Egg mass`, and the adult-unspecified `Whole body` are sibling concepts outside it. The definition should therefore not collapse the term to dissected gut, fecal material, egg masses, holometabolous larvae, pupae, prepupae, or the surrounding plant, soil, nest, water, or rearing substrate.

The label is ambiguous. `Nymph` names an immature insect in incomplete metamorphosis, and BTO's `BTO:0000954` reflects that organism-at-stage reading, which is why HabitatMech keeps it only as an `xref`, not as the habitat identity. `Instar` is broader: UC IPM defines it as a larval or nymph stage between successive molts, so a bare instar could be a larval instar in a butterfly or fly, not just a nymphal instar. The source path is the deciding context: GOLD already has separate `Larva`, `Prepupa`, and `Pupa` siblings under `Arthropoda: Insects`, so `Nymph/Instar` should be read as the nymphal-instared host bucket rather than all insect instars. ([ebi.ac.uk](https://www.ebi.ac.uk/?utm_source=openai))

That reading is supported by microbiome studies that treat nymphs as real host habitats: Olivier-Espejel et al. sampled nymphs and adults of the hemipteran giant mesquite bug and found a gut community dominated by environmentally acquired `Burkholderia` bacteria, and Malathi et al. profiled gut bacterial diversity in insecticide-susceptible and insecticide-resistant brown-planthopper nymphs using 16S amplicon sequencing. These are narrower gut studies, but they prove that nymphal insect bodies contain sampleable microbial habitats rather than only a developmental-time metadata value. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/?utm_source=openai))

**Genus**

The natural genus is `insect-associated environment`, already requested locally as `habitatmech:GOLD.dba2a83b95` and defined in [arthropoda_insects.yaml](/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/data/habitats/host_associated/arthropoda_insects.yaml) as an environmental system determined by an insect.

The smallest existing external ontology genus is `ENVO:01001002` `animal-associated environment`, whose ENVO definition is an environmental system determined by an animal. `ENVO:01001000` `environmental system determined by an organism` is correct but one level broader. The vendored ENVO slice contains organism-associated precedents such as animal-, plant-, fungal-, and cnidarian-associated environments, but no insect- or arthropod-associated environment, so `ENVO:01001002` is the right `parent_class` until ENVO gains the insect-scoped intermediate. ([ebi.ac.uk](https://www.ebi.ac.uk/?utm_source=openai))

Near-misses:

| Term | Why it fails |
|---|---|
| `BTO:0000954` `nymph` | Correct life-stage host, wrong entity type: it denotes the immature insect organism, not an environmental system determined by that organism. Keep as `xref`, matching the current decision row. |
| `UBERON:0002548` `larva` / `BTO:0000707` `larva` | Wrong sibling for GOLD. A larva is a juvenile form that proceeds through larval molts toward pupation; `Nymph/Instar` is paired with a separate `Larva` node and is for nymphal immatures. |
| `UBERON:0000069` `larval stage` | A life-cycle stage, not a sampled physical host body, and it is even farther from a host-associated environment. |
| `BTO:0001224` `second instar larva` | A narrower larval-stage class. It demonstrates the instar wording, but asserts both the wrong instar number and the wrong holometabolous side of insect development. |
| `ENVO:01001055` `environment associated with an animal part or small animal` | Broader than a nymphal insect and modeled around a disjunction of animal parts or whole small animals. It is not insect- or life-stage-specific. |
| `ENVO:01001176` `environment associated with an aquatic invertebrate` | Wrong axis: it covers aquatic invertebrate association, not terrestrial hemipteran, orthopteran, or blattodean nymphs. |
| `ENVO:01001002` `animal-associated environment` | The correct existing genus, but not an identity. Grounding here would merge this nymphal-insect habitat with every other animal host. |

**Differentia**

The defining differentia are:

| Differentia | Curation value |
|---|---|
| Host taxon | An insect, not a crustacean nauplius/zoea or a generic arthropod. This separates the term from crustacean larval-host records. |
| Developmental state | A nymphal instar: post-embryonic, pre-adult, and not yet fully adult-winged or reproductive. This separates it from eggs/embryos and adult `Whole body`. |
| Metamorphosis mode | Incomplete metamorphosis: no pupal stage. This separates it from the `Larva`, `Prepupa`, and `Pupa` siblings, which cover holometabolous insects. |
| Habitat granularity | The whole life-stage host environment. Gut and fecal samples are children/refinements; plant tissue, soil, water, nest material, and rearing substrate are surrounding or food environments. |

The first sentence should not say merely `instar-associated environment`: every larva has instars too. The safe phrase is `nymphal instar`, which preserves GOLD's slash label without absorbing larval instars.

**Sources To Cite**

| Claim | Source |
|---|---|
| `BTO:0000954` names the immature insect nymph, not a habitat. | BRENDA Tissue Ontology via OLS; retained by HabitatMech as an xref. ([ebi.ac.uk](https://www.ebi.ac.uk/?utm_source=openai)) |
| `instar` is a stage between molts and can apply to larval or nymphal stages. | University of California IPM glossary. ([ipm.ucanr.edu](https://ipm.ucanr.edu/?utm_source=openai)) |
| `ENVO:01001002` is `animal-associated environment`, defined as an environmental system determined by an animal. | ENVO via EBI OLS / OBO PURL. ([ebi.ac.uk](https://www.ebi.ac.uk/?utm_source=openai)) |
| Nymphal insects support sampleable gut microbiomes. | Olivier-Espejel et al. 2011, `Environmental Entomology` 40:1102-1110, DOI `10.1603/EN10309`, PMID `22251722`; Malathi et al. 2018, `Journal of Microbiology and Biotechnology` 28:976-986, DOI `10.4014/jmb.1711.11039`, PMID `29976032`. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/?utm_source=openai)) |

**Synonyms**

Exact or source-level synonyms:

| Synonym | Note |
|---|---|
| `Nymph/Instar` | GOLD source label. |
| `Nymph` | BTO xref label; acceptable as a record synonym, but the BTO term itself is an organism class. |
| `insect nymph-associated environment` | Clearer ontology-style label if ENVO asks for a HabitatMech term label. |
| `nymphal instar-associated environment` | Exact if the definition uses the nymphal-instar wording above. |

Related, narrower, or context labels that should not be exact synonyms:

| Term | Relationship |
|---|---|
| `first instar nymph`, `fifth instar nymph`, etc. | Stage-numbered subclasses of this concept. |
| `naiad` | Aquatic nymph of particular insect groups; narrower than the GOLD bin. |
| `hopper` | Grasshopper/locust nymph in ordinary use; narrower and order-specific. |

**Do Not Conflate With**

| Term | Why not |
|---|---|
| `instar` | A temporal growth interval between molts, and may be larval rather than nymphal. |
| `larva` / `larval instar` | Holometabolous or indirect-development sibling; GOLD has `Host-associated > Arthropoda: Insects > Larva` separately. |
| `prepupa`, `pupa`, `chrysalis`, `puparium` | Later holometabolous stages or coverings; outside incomplete-metamorphosis nymphs. |
| `egg`, `ootheca`, `embryo` | Pre-hatching or egg-mass concepts, not post-embryonic nymphs. |
| `adult`, `imago` | Adult stage after the final molt. |
| `nymphal gut`, `fecal`, `frass` | Part/material children of a nymphal host, not the broad host-stage habitat. |
| `larval habitat`, `breeding site`, `rearing substrate` | Surrounding environment or food substrate, not the insect host body. |

**Should This Be A Term?**

Yes, as a host-associated environment. The GOLD source concept is not merely a process, quality, or sampling artifact: it is a life-stage-qualified insect host used to organize host-associated microbial samples, with gut and fecal child records beneath it. It should stay minted under `habitatmech:GOLD.71e7bb35e2`, keep `BTO:0000954` only as an `xref`, and receive a definition row parallel to `insect larva-associated environment`, `insect prepupa-associated environment`, and `insect pupa-associated environment`.

My inference is the hemimetabolous/nymphal restriction. GOLD gives only the slash label `Nymph/Instar`; the reason to reject the broad `instar` reading is structural: the same insect subtree already has separate `Larva`, `Prepupa`, and `Pupa` siblings, so allowing larval instars here would duplicate that branch.

## Sources

- [BTO:0000954 nymph in EBI OLS](http://purl.obolibrary.org/obo/BTO_0000954)
- [ENVO:01001002 animal-associated environment in ENVO](http://purl.obolibrary.org/obo/ENVO_01001002)
- [University of California IPM Glossary](https://ipm.ucanr.edu/)
- [Olivier-Espejel et al. 2011, Gut Microbiota in Nymph and Adults of the Giant Mesquite Bug](https://doi.org/10.1603/EN10309)
- [Malathi et al. 2018, Gut Bacterial Diversity of Insecticide-Susceptible and -Resistant Nymphs of the Brown Planthopper](https://doi.org/10.4014/jmb.1711.11039)

## Limitations

- GOLD does not define the slash label. The nymphal-instar reading is an inference from its position under `Host-associated > Arthropoda: Insects` and from the presence of separate `Larva`, `Prepupa`, and `Pupa` siblings.
- I did not add `habitatmech:GOLD.71e7bb35e2` to `curation/term_requests.tsv`; the output above is definition evidence for a curator to apply.
