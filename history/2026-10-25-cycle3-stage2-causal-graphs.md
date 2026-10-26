# 2026-10-25 — Cycle 3 Stage 2 (`causal_graphs`): Audit of 43 Existing Causal Graphs and Authoring of 10 New Literature-Backed Habitat Mechanism Overlays

## Summary

Executed Cycle 3 Stage 2 (`causal_graphs`) of `mech-goal-sequence-20261019` using `.claude/skills/habitatmech-evolve-workflow/SKILL.md`, `.claude/skills/curate-causal-graphs/SKILL.md`, `.claude/skills/add-yaml-record/SKILL.md`, and `.claude/skills/curate-yaml-record/SKILL.md`:

1. **Full Audit of Existing 43 Curated Causal-Graph Overlays (`curation/causal_graphs/*.yaml`):**
   - Verified all 43 pre-existing overlays pass LinkML `HabitatCausalGraphCuration` validation, connected-component and root-`HABITAT` structural checks, ontology grounding correspondence (`conf/id_label_targets.yaml`), and verbatim evidence snippet cleanliness (no HTML artifacts or non-breaking spaces).
   - Preserved all Cycle 2 Stage 3 `GENE_OR_PROTEIN` verified `protein_examples` and source-limited multi-subunit/metagenomic boundary notes intact.

2. **Authored 10 New Evidence-Backed `HabitatCausalGraphCuration` Overlays (43 -> 53 total; 501 nodes, 499 edges, 579 evidence items):**
   - `curation/causal_graphs/permafrost.yaml` (`ENVO:00000134`, `TERRESTRIAL`): `permafrost_subzero_cryoadaptation_and_thaw_methanogenesis` — 5 nodes, 4 edges, 6 evidence items across 5 PubMed references (`PMID:20154119`, `PMID:25739499`, `PMID:38860762`, `PMID:34310124`, `PMID:37766397`).
   - `curation/causal_graphs/peatland.yaml` (`ENVO:00000044`, `TERRESTRIAL`): `peatland_acidiphilic_methanogenesis_and_type_ii_methanotrophy` — 5 nodes, 4 edges, 6 evidence items across 4 PubMed references (`PMID:20154331`, `PMID:25998264`, `PMID:18093158`, `PMID:19719661`).
   - `curation/causal_graphs/paddy_field_soil.yaml` (`ENVO:00005740`, `TERRESTRIAL`): `paddy_field_soil_rhizosphere_methanogenesis_and_methane_oxidation` — 4 nodes, 3 edges, 5 evidence items across 3 PubMed references (`PMID:14997675`, `PMID:38801181`, `PMID:41582156`).
   - `curation/causal_graphs/marine_salt_marsh_biome.yaml` (`ENVO:01000022`, `AQUATIC`): `marine_salt_marsh_spartina_sulfur_cycling_and_diazotrophy` — 4 nodes, 3 edges, 4 evidence items across 2 PubMed references (`PMID:35227326`, `PMID:18929068`).
   - `curation/causal_graphs/freshwater_biome.yaml` (`ENVO:00000873`, `AQUATIC`): `freshwater_biome_dom_photolysis_and_ph_bacterioplankton_sorting` — 4 nodes, 3 edges, 6 evidence items across 3 PubMed references (`PMID:20636377`, `PMID:22452571`, `PMID:33148818`).
   - `curation/causal_graphs/sea_grass_bed.yaml` (`ENVO:01000059`, `AQUATIC`): `sea_grass_bed_rhizosphere_rol_sulfide_and_nitrogen_cycling` — 4 nodes, 3 edges, 5 evidence items across 3 PubMed references (`PMID:29687545`, `PMID:40508259`, `PMID:39503478`).
   - `curation/causal_graphs/black_smoker.yaml` (`ENVO:00000218`, `AQUATIC`): `black_smoker_hydrothermal_chemolithoautotrophy_and_archaeoglobus_sulfate_reduction` — 4 nodes, 3 edges, 5 evidence items across 3 PubMed references (`PMID:24414410`, `PMID:28484604`, `PMID:34335500`).
   - `curation/causal_graphs/nectar.yaml` (`BTO:0000537`, `HOST_ASSOCIATED`): `nectar_osmotic_climatic_selection_and_pollinator_attractiveness` — 4 nodes, 3 edges, 5 evidence items across 2 PubMed references (`PMID:25041632`, `PMID:33370885`).
   - `curation/causal_graphs/pitcher.yaml` (`BTO:0001069`, `HOST_ASSOCIATED`): `pitcher_phytotelm_prey_digestion_and_diazotrophic_nutrient_supply` — 4 nodes, 3 edges, 7 evidence items across 4 PubMed references (`PMID:35734258`, `PMID:35384233`, `PMID:38995889`, `PMID:38441172`).
   - `curation/causal_graphs/sewage.yaml` (`ENVO:00002018`, `ENGINEERED`): `sewage_conveyance_selection_and_antibiotic_resistance_reservoir` — 4 nodes, 3 edges, 6 evidence items across 2 PubMed references (`PMID:35762794`, `PMID:30682717`).

3. **Native Regeneration and Validation:**
   - Regenerated all 3,209 habitat records via `scripts/seed_from_sources.py --apply --force` (`curated_causal_graphs_loaded: 53`), rendered all HTML pages via `scripts/render_pages.py`, and synchronized documentation stats blocks via `scripts/check_docs.py --write`.
   - Added regression tests in `tests/test_stage2_causal_graph_curation.py` verifying all 10 new Cycle 3 Stage 2 overlays and the 53-graph total.
