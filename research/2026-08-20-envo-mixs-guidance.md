<!--
Snapshot of ENVO's "Using ENVO with MIxS" wiki page, fetched 2026-08-20 from
https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS

Committed because CLAUDE.md now quotes it for rules this corpus previously
asserted in its own voice (#127). A wiki page can change or vanish; a rule
citing a source that no longer says what it said is worse than one that never
cited anything.
-->

# General notes and guidance
The [Minimum Information about any (x) Sequence (MIxS)](https://gensc.org/mixs/) is a checklist from the [Genomic Standards Consortium](https://gensc.org/mixs/). This checklist features three mandatory fields for environmental description using ENVO classes. 



# Guidance for MIxS version 5
This guidance is relevant to version 5 of the MIxS checklist, available as an XLSX document, [here](press3.mcs.anl.gov/gensc/files/2020/02/mixs_v5.xlsx)

Field name | Full name | Description | Comments 
---|---|---|---
env_broad_scale | broad-scale environmental context | In this field, report which major environmental system your sample or specimen came from. The systems identified should have a coarse spatial grain, to provide the general environmental context of where the sampling was done (e.g. were you in the desert or a rainforest?). | We recommend using subclasses of ENVO’s biome class: http://purl.obolibrary.org/obo/ENVO_00000428
env_local_scale	| local environmental context | In this field, report the entity or entities which are in your sample or specimen’s local vicinity and which you believe have significant causal influences on your sample or specimen. | Please use terms that are present in ENVO and which are of smaller spatial grain than your entry for env_broad_scale
env_medium | environmental medium | In this field, report which environmental material or materials (pipe separated) immediately surrounded your sample or specimen prior to sampling | Please use one or more subclasses of ENVO’s environmental material class: http://purl.obolibrary.org/obo/ENVO_00010483.

## Finding the right terms for each MIxS field

* `env_broad_scale` should really focus on the big, contextualising environment. Was the sample from a desert or the tundra? This term should describe an environmental system or an ecosystem, not a process, material, or single object (e.g. a tree) or a group of objects (e.g. a stand of trees).
* `env_local_scale` should include those environmental entities that surround your sample material and are likely to causally influence it. The terms used here should be countable things (e.g. a rock, a snow crystal, a cave, a hydrothermal vent.)
* `env_medium` should always refer to the materials that compose your sample or which your entity of interest are surrounded by. These should always be mass/volume nouns (e.g. a mass/volume of "soil", "water", or "tissue") and **not** terms that refer to countable entities (e.g. a "cuticle", "microbial mat", "tree").

If you need to use a class from another ontology (e.g. a type of tissue material from an anatomy ontology), see "Notes on the use of other ontologies in MIxS environment fields", below.

## Format

The valid format includes the term label, followed by a space, and then the term's ID in CURIE format. 

Format (single term) | Format (multiple terms)
---|---
termLabel [termID] | termLabel [termID]\|termLabel [termID]\|termLabel [termID]

Example: single term | Example: multiple terms
---|---
tropical moist broadleaf forest biome [ENVO:01000228] | canopy [ENVO:00000047]\|herb and fern layer [ENVO:01000337]




## Example annotations

Consider a sample of leaf litter taken from the understory of the Amazon rainforest. An appropriate annotation would be:

```
env_broad_scale : tropical moist broadleaf forest biome [ENVO:01000228]
env_local_scale : understory [ENVO:01000335]
env_medium      : plant matter [ENVO:01001121]
```
If this was a sample of plant matter pooled from several layers of the forest's vegetation, a valid annotation may resemble: 

```
env_broad_scale : tropical moist broadleaf forest biome [ENVO:01000228]
env_local_scale : canopy [ENVO:00000047]|herb and fern layer [ENVO:01000337]|litter layer [ENVO:01000338]|understory [01000335]|shrub layer [ENVO:01000336] 
env_medium      : plant matter [ENVO:01001121]
```

Consider the following annotation for a water sample from a seasonal thermocline in the well-lit waters of the Atlantic Ocean: 
```
env_broad_scale : oceanic epipelagic zone biome [ENVO:01000033]
env_local_scale : seasonal thermocline [ENVO:01000107]
env_medium      : ocean water [ENVO:00002151]
```
 
If one is dealing with larger organisms, multiple env_medium terms may be needed. For example, consider a duck paddling in water:

```
env_medium : pond water [ENVO:00002228]|air [ENVO_00002005]
```

## Requesting new terms

If needed, request new terms on the [ENVO tracker](https://github.com/EnvironmentOntology/envo/issues).
Please include a definition of the new term (see our guidance on definitions, [here](https://github.com/EnvironmentOntology/envo/wiki/Creating-good-definitions)), citing relevant sources.

If you plan to add a lot of new terms, please consult [this page](https://github.com/EnvironmentOntology/envo/wiki/Adding-classes-to-ENVO).

## Differentiating between environmental context and sample processing

At times, the sampling method used can enrich or deplete certain organisms or otherwise modify the environmental material (env_medium) in the sample. For example, a filtration net dragged through seawater to enrich organisms larger than the spaces in the net weave. 

The env_medium field is meant to capture the original material sampled, rather than what subsequently happened to that material during or after sampling.
Please add information or links to protocols on the effects of sampling on the original material sampled, to MIxS fields such as:

```
samp_collect_device
samp_mat_process
size_frac
samp_size 
```

## Notes on annotating microscale or microbial samples

Many MIxS users will be working with microbial communities. We offer the following recommendations for these users:

### General considerations

* When filling in the `env_broad_scale` field, it's tempting to assume that macroscale environments do not matter to the microbial assemblage sampled. Nonetheless, we strongly encourage these larger scale systems (e.g. urban biomes or subtropical desert biomes) to be identified, in addition to any smaller scale features. These annotations will be instrumental for leveraging data in global analyses and for microbial biogeography. Keep in mind, users can always include any smaller-scale environments using the multi-term format noted above.
* When filling in the `env_local_scale` field, attempt to add new, more fine-grained information relative to the `env_broad_scale` field. For example, a MIxS entry that includes `env_broad_scale: village biome [ENVO:01000246]` and `env_local_scale: village [ENVO:01000773]` is not as useful as one that includes `env_broad_scale: village biome [ENVO:01000246]` and `env_local_scale: farm [ENVO:00000078]`

### Host-associated microbial samples

#### General advice

* When annotating microbial communities living in or on *host organisms*, we recommend the following:
  * Ensure the taxonomic information of the host (e.g. the NCBI TaxID) is filled out in the MIxS host fields.
  * `env_broad_scale` entries should reflect the ecosystem the host is found in (e.g. an urban biome [ENVO:01000249] or a tundra biome [ENVO:01000180])
  * `env_local_scale` entries should use terms from an ontology such as [UBERON](http://obofoundry.org/ontology/uberon.html) or [PO](http://obofoundry.org/ontology/po.html) to describe the anatomical parts of the host that are most causally influential to the microbial communities sampled (e.g. skin of eyelid [UBERON:0001457] or tepal apex [PO:0025143])
  * `env_medium` should either be a term from the ENVO [environmental material](http://purl.obolibrary.org/obo/ENVO_00010483) hierarchy, or one from the anatomical ontologies relevant to the host organism.

## Notes on the use of other ontologies in MIxS environment fields

ENVO won't have every term that you need, and we wouldn't import terms from other ontologies that we already interoperate with.
Thus, you can use terms from other [OBO ontologies](http://obofoundry.org/) (such as [PO](http://obofoundry.org/ontology/po.html) and [UBERON](http://obofoundry.org/ontology/uberon.html)) in MIxS `env_broad_scale`, `env_local_scale`, or `env_medium` fields, **as long as they fit the same logic described in [Finding the right terms for each MIxS field](https://github.com/EnvironmentOntology/envo/wiki/ENVO-annotations-for-MIxS-v5#finding-the-right-terms-for-each-mixs-field)**.

However, note that some resources in the OBO catalogue are not appropriate for these MIxS fields. For example, OBO's port of the [NCBI Taxonomy](http://obofoundry.org/ontology/ncbitaxon.html) is not appropriate, as taxonomic information can and should be contained in other MIxS fields. We also do not recommend using ports of thesauri and glossaries such as the [NCIT](http://obofoundry.org/ontology/ncit.html)

#### Advanced usage
If you're writing code that needs precise environmental semantics using terms from outside of ENVO, we recommend that you post-compose such semantics using patterns like:
* 'liver ecosystem' = ecosystem [ENVO:01001110] and [determined by](http://purl.obolibrary.org/obo/RO_0002507) some liver [UBERON:0002107]
* 'mucus material' = 'environmental material' [ENVO:00010483] and [composed primarily of](http://purl.obolibrary.org/obo/RO_0002473) some mucus [UBERON:0000912]