---
provider: claude_code
model: claude-fable-5-1, claude-haiku-4-5-20251001
cached: false
start_time: '2026-09-08T17:41:46.130626'
end_time: '2026-09-08T18:57:13.493548'
duration_seconds: 4527.36
template_file: templates/habitat_definition_research.md
template_variables:
  habitat_label: Carbonate
  habitat_identifier: habitatmech:GOLD.1208484062
  habitat_category: AQUATIC
  grounding_status: UNGROUNDED
  attestations: 'GOLD: Environmental > Aquatic > Non-marine Saline and Alkaline >
    Alkaline > Carbonate'
  assertions: '12'
  parent_terms: (none)
  xrefs: (none)
  decision_note: 'Confirmed UNGROUNDED: no ontology term fits this concept. Non-habitat
    screen review (#108): in Environmental > Aquatic > Non-marine Saline and Alkaline
    > Alkaline > Carbonate, the leaf scopes an alkaline carbonate-rich aquatic environment;
    it does not claim that the carbonate ion itself is the habitat. An external chemical
    term is external evidence for the modifier and is not in the committed slice.
    (source concept habitatmech:GOLD.1208484062)'
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
  - claude-fable-5-1
  - claude-haiku-4-5-20251001
  web_search_requests: 8
  num_turns: 48
  total_cost_usd: 5.27204025
  session_id: 8e03a032-d37f-4e6d-9cdd-a7a2d4ebe016
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 2
---

## Question

# HabitatMech Novel-Term Definition Research

## Target concept

- **Label as the source names it:** Carbonate
- **HabitatMech identifier (already a CURIE — quote it verbatim, do not prefix it):** habitatmech:GOLD.1208484062
- **Category:** AQUATIC
- **Grounding status:** UNGROUNDED
- **Source attestations:** GOLD: Environmental > Aquatic > Non-marine Saline and Alkaline > Alkaline > Carbonate
- **Upstream assertion volume:** 12
- **Nearest broader term already on the record:** (none)
- **Cross-references upstream suggested:** (none)

## Why this concept has no term

HabitatMech mints an identifier only when no term in ENVO, UBERON, FOODON, BTO or PO
names the concept. This one is unnamed, so HabitatMech has to supply the definition
itself. The curator's note recorded on the decision is:

> Confirmed UNGROUNDED: no ontology term fits this concept. Non-habitat screen review (#108): in Environmental > Aquatic > Non-marine Saline and Alkaline > Alkaline > Carbonate, the leaf scopes an alkaline carbonate-rich aquatic environment; it does not claim that the carbonate ion itself is the habitat. An external chemical term is external evidence for the modifier and is not in the committed slice. (source concept habitatmech:GOLD.1208484062)

## Research objective

Produce the material a curator needs to write an **Aristotelian genus-differentia
definition** for **Carbonate** as a microbial habitat, with citations.

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

I'll research the GOLD "Carbonate" leaf, check the repo for sibling records, and search the literature and ENVO for genus candidates.

# Research report: "Carbonate" (habitatmech:GOLD.1208484062)

## Proposed definition

> A marine hydrothermal vent chimney which is built of brucite and calcium and magnesium carbonates precipitated where low-temperature, hyperalkaline, hydrogen- and methane-rich fluid produced by serpentinization of ultramafic rock mixes with seawater.

Genus: ENVO:01000129 "marine hydrothermal vent chimney" (present in the committed slice). The differentia is mineralogy plus fluid origin. Both are measurable and both are stated by the sources below.

**Headline finding.** The curator's recorded reading ("an alkaline carbonate-rich aquatic environment", i.e. soda-lake-like water) does not match the GOLD data. Every organism GOLD files under this leaf was isolated from carbonate chimneys of the Prony Hydrothermal Field in New Caledonia, a serpentinization-driven vent system. "Carbonate" here is the carbonate chimney as a material and landform, not carbonate-rich water. This changes the genus from a lake or water term to a chimney term.

## 1. What the concept denotes

**Evidence from GOLD itself.** The GOLD bulk export (goldData.xlsx, October 2021 copy at `/Users/marcin/Documents/VIMSS/ontology/Sample/GOLD/goldData.xlsx`, streamed with the repo's own reader from `scripts/extract_gold_biosamples.py`) contains 10 Organism rows with ecosystem path id 3969, which is the `gold.ecosystem:3969` on this record. Their sample-collection sites are all "Carbonate chimney in Prony Hydrothermal Field" or "ST09 PHF hydrothermal chimney". No Biosample rows carry the path. The organisms:

| GOLD ID | Organism | Collection site (verbatim) |
|---|---|---|
| Go0118393, Go0473086 | *Alkaliphilus* sp. LacV | ST09 PHF hydrothermal chimney / Carbonate chimney in Prony Hydrothermal Field |
| Go0118395, Go0473092 | *Alkaliphilus* sp. LacT | same |
| Go0473085 | *Alkaliphilus hydrothermalis* FatMR1 | Carbonate chimney in Prony Hydrothermal Field |
| Go0473087 | *Alkaliphilus halophilus* Alk_halo | same |
| Go0473088 | *Acetoanaerobium pronyense* Clo_St07-YE | same |
| Go0473089 | *Serpentinicella alkaliphila* Alk_3B | same |
| Go0473090 | *Alkaliphilus crotonatoxidans* Alk_croto | same |
| Go0473091 | *Alkaliphilus peptidifermentans* Alk_pepti | same |

The current corpus counts 12 organism assertions from the 2026 export. I could inspect only the 2021 copy, so 2 later rows are unverified. All 10 inspected rows point to the same site and the published isolate descriptions confirm it (Ben Aissa et al. 2015; Bes et al. 2015; Mei et al. 2016; Postec et al. 2021, cited in section 4).

**What the place is.** The Prony Bay Hydrothermal Field discharges "hydrogen- and methane-rich fluids with low salinity, temperature (< 40°C) and high pH (11) produced by the serpentinization reactions of the ultramafic basement into the lagoon seawater. They are responsible for the formation of carbonate chimneys at the lagoon seafloor" (Quéméneur et al. 2014, doi:10.1111/1758-2229.12184). The fluids are "hyperalkaline freshwaters of the Ca-OH type (pH 11)" of meteoric origin; salinity is as low as 0.3 g/L, and emitted gas is 12 to 30% H2 and 6 to 14% CH4 (Monnin et al. 2014, doi:10.5194/bg-11-5687-2014). Chimneys are porous structures "mainly made of brucite along with carbonates" with more calcium carbonate toward the exterior where seawater mixing occurs (Pisapia et al. 2017, doi:10.3389/fmicb.2017.00057). Vents lie at depths to 50 m, and additional sites are intertidal and exposed at low tide (Monnin et al. 2014; Frouin et al. 2018, doi:10.3389/fmicb.2018.00102).

**Boundary.** Inside the concept: the solid chimney or edifice (its interior conduits, brown mats in them, and the brucite-carbonate matrix), sampled for isolation or sequencing. Neighbouring concepts, outside: the venting fluid itself (a hyperalkaline water), the surrounding lagoon seawater, the serpentinized peridotite basement, and the onshore hyperalkaline springs of New Caledonia that are not submarine (Quéméneur et al. 2023, doi:10.3389/fmicb.2023.1196516).

**Ambiguity.** The label alone admits three readings. (a) Soda-lake or carbonate-alkaline water; this is what the earlier curator note assumed and what the sibling GOLD nodes (Sediment, Microbial mats, Mine pit pond) might suggest. (b) Carbonate precipitates such as microbialites or tufa in alkaline lakes. (c) Serpentinization-hosted carbonate chimneys. The organism records settle it as (c). Reading (a) is supported by nothing in the data attached to this leaf.

**A tension to record.** GOLD places the leaf under "Non-marine Saline and Alkaline", presumably because the fluid is meteoric and non-saline. The chimneys themselves stand in lagoon seawater or in the intertidal zone. The literature calls the setting "shallow marine" (Postec et al. 2015, doi:10.3389/fmicb.2015.00857) and "coastal" with "both submarine and intertidal active sites" (Frouin et al. 2018). The definition should follow the literature and the mineral-forming process, and the GOLD path should be preserved only as the attestation.

## 2. Genus

**Recommended genus: ENVO:01000129 "marine hydrothermal vent chimney".** ENVO definition: "A column of solid material which has been progressively deposited around a hydrothermal vent." Parent in ENVO: ENVO:01001885 "submerged landform". No children, no synonyms. It is in the committed slice. Prony chimneys satisfy this definition literally; the concept is narrower because it fixes the mineralogy and the fluid source, so ENVO:01000129 is strictly broader.

A curator could also argue for grounding directly to ENVO:01000129 rather than minting. I recommend against it, because the GOLD leaf plainly excludes sulfide and anhydrite chimneys of black and white smokers, and the alkaliphilic community differs from those. Keeping the minted identity with ENVO:01000129 as `parent_habitats` preserves the distinction.

**Near-misses, and why each fails:**

- ENVO:01000257 "white smoker". Its definition speaks of barium, calcium and silicon minerals and "alkaline hydrothermal vents", but white smokers are volcanically driven and hotter. Serpentinite-hosted carbonate chimneys are a distinct class (Kelley et al. 2005, doi:10.1126/science.1102556). Not a match.
- ENVO:00000215 "hydrothermal vent" and ENVO:01000122 "marine hydrothermal vent". These are the fissure or benthic feature, not the deposited solid. Broader than the genus above and less specific. Use as xref only if the chimney term is rejected.
- ENVO:01000053 "marine ultramafic hydrothermal vent biome". A biome, not a material or landform. Correct as a broad-scale triad value or xref, wrong as identity.
- ENVO:00002121 "alkaline salt lake" (exact synonym "soda lake"). This is the near-miss for the curator's earlier reading. Its parent is ENVO:00000019 "saline lake". It asserts a lake, which the data does not support.
- ENVO:01000357 "alkaline water". A material with pH above 7. The venting fluid is alkaline water, but the sampled thing is the chimney.
- ENVO:03600064 "microbialite". Carbonate mud rock formed by benthic microbes. Prony chimneys form by abiotic mixing precipitation with some microbial mineralization (Pisapia et al. 2017). Not the same class.
- ENVO:00003982 "travertine" and ENVO:00002053 "limestone". Spring-deposited or sedimentary calcium carbonate rock. Neither captures brucite or the hydrothermal vent setting.
- ENVO:01001895 "soda spring". Defined by elevated dissolved CO2, which is the opposite of the CO2-depleted Ca-OH fluid here.
- No ENVO term for "serpentinization", "serpentinite-hosted", or "alkaline hydrothermal vent" exists (OLS search, September 2026, returned nothing for "serpentin").

## 3. Differentia

Properties that separate this chimney from other members of ENVO:01000129:

- **Mineralogy.** Brucite [Mg(OH)2] with aragonite, calcite and magnesium carbonates, calcium carbonates increasing outward (Pisapia et al. 2017; Postec et al. 2015). Smoker chimneys are sulfide and sulfate minerals.
- **Fluid origin and chemistry.** Serpentinization of ultramafic (peridotite) rock by meteoric water; Ca-OH type, pH about 11, below 40 °C, salinity down to 0.3 g/L, H2 and CH4 rich (Monnin et al. 2014; Quéméneur et al. 2014).
- **Formation process.** Precipitation where the hyperalkaline fluid mixes with seawater; brucite begins forming near pH 10 and Mg and Mg-Ca carbonates are strongly supersaturated (Monnin et al. 2014).
- **Setting.** Shallow submarine, 0 to 50 m, and intertidal (Monnin et al. 2014; Frouin et al. 2018). Lost City, the deep-sea analogue, is at about 800 m and 40 to 90 °C (Kelley et al. 2005; Postec et al. 2015).
- **Community.** Archaea dominated by uncultured Methanosarcinales shared with Lost City and The Cedars; bacteria dominated by Chloroflexi, Firmicutes and Proteobacteria; cultured isolates are anaerobic alkaliphiles of *Alkaliphilus*, *Serpentinicella* and *Acetoanaerobium* with pH optima 8.2 to 9.5 (Quéméneur et al. 2014; Frouin et al. 2018; isolate papers below).

Inference, not stated by any source: that the GOLD leaf is meant to cover carbonate chimneys of any serpentinite-hosted field (Lost City, Old City, Strýtan) and not only Prony. The data attached so far is Prony only. The proposed definition is written at the class level so that other fields would fit.

## 4. Sources

| Claim | Source |
|---|---|
| Organisms under path 3969 are Prony chimney isolates | GOLD bulk export, Organism sheet, columns ORGANISM ECOSYSTEM PATH ID and ORGANISM SAMPLE COLLECTION SITE (local copy dated 2021-10-04; download page https://gold.jgi.doe.gov/download?mode=site_excel) |
| Fluids pH 11, <40 °C, low salinity, H2/CH4 rich, form carbonate chimneys on lagoon seafloor | Quéméneur M et al. 2014. Environ Microbiol Rep. doi:10.1111/1758-2229.12184. PMID 25756120 |
| Ca-OH fluid, meteoric origin, salinity 0.3 g/L, gas composition, brucite and carbonate supersaturation on mixing, depths to 50 m, intertidal sites | Monnin C et al. 2014. Biogeosciences 11:5687. doi:10.5194/bg-11-5687-2014 |
| Shallow marine 30 to 50 m, meteoric origin, chimney minerals, dominant taxa, Lost City comparison | Postec A et al. 2015. Front Microbiol 6:857. doi:10.3389/fmicb.2015.00857. PMC4551099 |
| Brucite plus aragonite chimneys, calcium carbonate toward exterior, pH >9.5, T <40 °C, serpentinization-based ecosystems | Pisapia C et al. 2017. Front Microbiol 8:57. doi:10.3389/fmicb.2017.00057. PMID 28197130 |
| Coastal field with submarine and intertidal chimneys, porous carbonate edifices, community structure | Frouin E et al. 2018. Front Microbiol 9:102. doi:10.3389/fmicb.2018.00102. PMC5808123 |
| Hydrogen-producing Firmicutes, intertidal vs submarine | Mei N et al. 2016. Front Microbiol 7:1301. doi:10.3389/fmicb.2016.01301 |
| *Alkaliphilus hydrothermalis* from a Prony carbonaceous chimney | Ben Aissa F et al. 2015. Extremophiles. doi:10.1007/s00792-014-0697-y. PMID 25319677 |
| *Acetoanaerobium pronyense* from a Prony carbonate chimney | Bes M et al. 2015. Int J Syst Evol Microbiol. doi:10.1099/ijs.0.000307. PMID 25948619 |
| *Serpentinicella alkaliphila* from a Prony carbonaceous chimney | Mei N et al. 2016. Int J Syst Evol Microbiol. doi:10.1099/ijsem.0.001375. PMID 27499124 |
| *Alkaliphilus serpentinus* and *A. pronyensis* (strains LacT, LacV) from Prony | Postec A et al. 2021. Syst Appl Microbiol. doi:10.1016/j.syapm.2020.126175. PMID 33422701 |
| Serpentinite-hosted carbonate chimneys as a class; Lost City pH 9 to 11, <40 to 90 °C | Kelley DS et al. 2005. Science 307:1428. doi:10.1126/science.1102556 |
| Review of serpentinite-hosted microbial ecology, 2025 | Colman DR et al. 2025. ISME J. doi:10.1093/ismejo/wraf029. PMID 39961017 |
| Onshore New Caledonia hyperalkaline springs (neighbouring concept) | Quéméneur M et al. 2023. Front Microbiol. doi:10.3389/fmicb.2023.1196516. PMC10359428 |
| ENVO term definitions, parents, synonyms | OLS4 API, https://www.ebi.ac.uk/ols4/ontologies/envo, queried 2026-09-08; committed slice `data/raw/ontology_terms.tsv` |
| Soda lake definitions (for the rejected reading) | Sorokin DY et al. 2014. Extremophiles. doi:10.1007/s00792-014-0670-9; Boros E, Kolpakova M 2018. PLoS ONE. doi:10.1371/journal.pone.0202205; Vavourakis CD et al. 2016. Front Microbiol. doi:10.3389/fmicb.2016.00211 |

## 5. Synonyms and what not to conflate

**Names in real use for this concept:** carbonate chimney; carbonaceous chimney; carbonate edifice; hydrothermal chimney (in the Prony literature); serpentinite-hosted hydrothermal chimney; alkaline vent chimney; Lost City-type chimney (by analogy).

**Do not conflate with:**

- Soda lake or alkaline salt lake (ENVO:00002121). Sodium carbonate brine, evaporative origin, a lake. Boros and Kolpakova 2018 define it by Na and HCO3 + CO3 ionic dominance above 25 equivalent percent. Different genus entirely.
- Carbonate ion (CHEBI:41609), sodium carbonate (CHEBI:29377), hydrogencarbonate (CHEBI:17544). Chemical entities, not habitats. Useful at most as an xref to explain the label.
- Limestone, travertine, tufa, marl (ENVO:00002053, ENVO:00003982, ENVO:01000853). Carbonate rocks with different origins.
- Microbialite (ENVO:03600064). Benthic microbially mediated carbonate mud rock in lakes.
- Black smoker and white smoker (ENVO:00000218, ENVO:01000257). Volcanically driven, hot, sulfide or sulfate chimneys.
- Hyperalkaline spring on land (ENVO:01001894 "alkaline spring"). Same serpentinization chemistry, but no submarine chimney and no seawater mixing.
- Alkaline hot spring (ENVO:00002119). Geothermal, not serpentinization.
- Soda spring (ENVO:01001895). CO2-rich, which is the opposite chemistry.

## 6. Whether it should be a term

Yes. It is a physical material and landform that samples are taken from, with a well-described formation process, mineralogy and community. It is not a quality, a process, a chemical or a sampling artefact. The record should stay minted and UNGROUNDED, with these changes to consider:

- Add ENVO:01000129 "marine hydrothermal vent chimney" as a strictly broader parent. The current parent is the "Alkaline" node (habitatmech:GOLD.94b8786010), which the corpus already marks NOT_APPLICABLE, so the record now has no habitat parent.
- Add ENVO:01000053 "marine ultramafic hydrothermal vent biome" and ENVO:01000357 "alkaline water" as xrefs, not parents.
- Replace the decision note. The current note's "alkaline carbonate-rich aquatic environment" reading is not supported by any organism attached to the leaf and would mislead a later curator toward soda lakes.
- Flag the GOLD "Non-marine" placement as a source classification artefact rather than adopting it in the definition.

**What I could not verify.** The 2 organism rows added between the 2021 export and the 2026 export used by the corpus. The GOLD website returned 403 to fetches, so I could not read the live organism pages. If a later addition is not a Prony chimney isolate, the class-level wording above still holds, but a curator should check the two rows before committing the definition.

## Citations

1. https://gold.jgi.doe.gov/download?mode=site_excel
2. https://www.ebi.ac.uk/ols4/ontologies/envo