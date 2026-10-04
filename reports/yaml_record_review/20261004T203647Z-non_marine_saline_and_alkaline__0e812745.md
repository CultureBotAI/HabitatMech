# YAML Record Review: inland saline or alkaline aquatic environment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/non_marine_saline_and_alkaline__0e812745.yaml`
- Started UTC: 2026-10-04T20:30:29Z
- Finished UTC: 2026-10-04T20:36:47Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.ce244e62cd, AQUATIC,
UNGROUNDED/REVIEWED. It contains an authored definition, four exact synonyms,
one ontology parent, two source attestations, 25 BacDive taxon associations
and four history events. Parameters, xrefs, record-level evidence, graphs,
discussions and datasets are absent. `PATHS.tsv:2807` pins the stem.

Source concepts are GOLD `Environmental > Aquatic > Non-marine Saline and Alkaline`
and bacdive.isolation_source:non-marine-saline-and-alkaline. Actual minting
gives habitatmech:GOLD.ce244e62cd and habitatmech:BACDIVE.9a0a53afc1.
The latter merges into the former. This is the curated disjunctive aquatic
setting, not its bare Alkaline or Near-boiling qualifier children.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/non_marine_saline_and_alkaline__0e812745.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/non_marine_saline_and_alkaline__0e812745.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Fresh shared PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records and 1,810 decisions. |
| `just qc` | Fresh batch run active in tests; lint, documentation and all 14 raw inventories passed. No terminal result claimed. |
| Source/reference checks | Full target, maintained rows and research report; actual full-corpus build and field equality; both resolver/decision routes; 14 raw tables; current typed ENVO/OLS, PATO, all 25 NCBI taxa, three GOLD nodes, nine study attempts, primary publication and three BacDive records; full page/semantic comparison. |

All emitted target fields, including complete taxon/attestation dictionaries,
synonyms and all four history events, equal the actual build. Reproduction
does not prove the curated synonyms scientifically exact. No SSSOM/KGX
consumer/export compatibility audit was performed. Later terminal QC belongs
in the publication receipt rather than being backdated into this report.

## Identity and Grounding

`curation/decisions.tsv:1597` supplies GOLD's ITEM CONFIRM_UNGROUNDED;
`:1600` supplies BacDive's ITEM SAME_AS, both dated 2026-08-25. Actual
GOLD default resolution is gold_unmatched/UNGROUNDED/no predicate. Applying
the decision retains its ID and adds ENVO:01000317, reviewed=True.
BacDive defaults to bacdive_non_habitat_target/NOT_APPLICABLE with a
PATO:0001430 xref. SAME_AS instead contributes the GOLD survivor,
contributes_grounding=False, reviewed=True, no xref and no predicate.
The current PATO term is an acidity quality, not this habitat identity.

Actual construction counts two source concepts and two reviewed sources.
The survivor is genuinely REVIEWED; the discarded quality mapping does not
overwrite its UNGROUNDED state. The note explaining omitted PATO is accurate.
No narrowMatch is emitted, so this is not a current #1398 witness.

`curation/term_requests.tsv:43` owns the definition and REPLACE parent mode.
Current [ENVO:01000317 aquatic environment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000317)
is active and supports a water-influenced setting. The old aquatic-biome
parent is absent as intended by closed #185. Raw depth-four children include
Saline, Alkaline, lakes and operated settings; the source classification is
not itself a claim about ecological climax communities. Keep the justified
genus and documented replacement, not the discarded biome edge.

The definition's inland, saline OR alkaline OR both reading is explicit
curator interpretation. It must not be silently replaced by saline AND
alkaline, nor used to endorse all source descendants. Contemporary
[GOLD guidance](https://gold.jgi.doe.gov/ecosystem_classification) says its
paths describe collection surroundings and are sample-driven, not an
exhaustive formal ontology. Source-context nesting alone does not prove is-a.

Three authored EXACT_SYNONYM strings do not preserve the defined extension:
`inland saline waters`, `saline inland waters` and `continental saline waters`
name the saline arm, omitting alkaline-only settings. The research report
calls these approximate names before recommending exactness, an unsupported
promotion inherited by the maintained row. Current ENVO separately models
saline environment (ENVO:01001040) and alkaline environment (ENVO:01000316).
Neither alone supplies identity for their geographically restricted union.

The inspected [Boros and Kolpakova study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0202205)
uses an explicit saline-water sample selection and distinguishes chemical
type from pH; it does not establish those names as exact synonyms for all
alkaline-only aquatic settings. This scope diagnosis is an inference from
the authored disjunction and inspected source definitions, not a claim that
the paper directly adjudicates HabitatMech synonyms. Do not narrow the whole
record merely to make those aliases exact.

## Evidence

Physical `gold_ecosystem_paths.tsv:176` gives depth three, nodes 3482, 3752
and 3970, 121 organisms and zero study/biosample counters. The displayed
gold.ecosystem:3482 and three-node note match. `bacdive_isolation_sources.tsv:102`
gives 37 STRAIN assertions and 28 taxa. These are different source units,
not 158 organisms, samples or independent experiments.

`gold_path_biosamples.tsv:288` separately gives 74 bulk samples at node
3970. Triad rows 686-688 summarize 66 complete-triad API samples in six
studies, with independently verified current terms:

| Role | Modal term | Share | Distinct terms | Agreeing studies |
| --- | --- | ---: | ---: | ---: |
| Broad | ENVO:00002030 aquatic biome | 0.98 | 2 | 5 |
| Local | ENVO:00000019 saline lake | 0.79 | 7 | 1 |
| Medium | ENVO:04000007 lake water | 0.82 | 6 | 2 |

The secondary terms are not supplied here. Modal terms are contextual,
not replacement identities, universal properties or measured limits. The
66/74 totals are not a verified exact-sample crosswalk. Nine study memberships
occur at gold_studies.tsv physical rows 91, 189, 390, 978, 979, 1456, 1560,
2606 and 3103: Gs0046169, Gs0053056, Gs0067861, Gs0117923, Gs0117924,
Gs0128714, Gs0129073, Gs0144745 and Gs0150279. Every original study request
returned 403. Several studies span other habitats; their full experiments
were not recovered or attributed wholesale to this target.

Current GOLD 3482 and 3752 returned 404, not proof of retirement. Node 3970
is active with the exact path and partial aquatic-biome annotation only;
no local/medium field is supplied there. The complete 14-table exact-source
scan found no environmental-parameter, PREGO or MADIN contribution.

All 25 BacDive taxon rows at `bacdive_source_taxa.tsv:1989-2013` match the
complete generated dictionaries. The extractor counts distinct linked strains
per taxon, ranks by descending count then taxon ID, and retains 25 of a pool
of 28. Counts are 5, 3, 2, 2, 2 and then twenty ones. Tied ranks do not
establish different evidence strength; three omitted taxa are not absent
biologically. No entry asserts is_characteristic or cross-source corroboration.

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=83428,2183934,1872700,1926584,617000,1008392,1227484,1227493,1246445,1454184,1586233,1721088,1807133,1812810,1871618,1874361,2024860,263724,2746,393481,411959,488938,555779,589865,617001&retmode=xml)
resolved all 25 IDs directly with matching names and no alias redirects.
Five IDs are explicitly strain-ranked; the broad sp./uncultured labels must
not be promoted to identified species or a homogeneous taxonomic rank.
This checks identity, not ecological representativeness.

Original BacDive pages provide bounded examples: [4066](https://bacdive.dsmz.de/strain/4066)
links NCBITaxon:617001 and this category to soda-lake sediment;
[140048](https://bacdive.dsmz.de/strain/140048) links 2183934 to Kulunda
soda lakes; [158350](https://bacdive.dsmz.de/strain/158350) links 1721088
to saline-lake water. Their culture media, growth limits and automated
predictions are not measurements of this whole habitat. These three pages
do not independently reverify every historical 37-strain link or all 25
associations. The original transformed BacDive nodes/edges were not found
in the configured kg-microbe checkout by a gitignore-independent filename
search; notebooks and old pickle files are not the manifest-pinned inputs.

## Completeness

Ignored-inclusive source keys, three nodes, old/new labels, path and stem
searches covered curation, history, research, reports, conf, PATHS and
RETIRED, plus filename inventory. They found the two ITEM rows, term request,
complete research report and both retirement redirects, but no target-owned
causal overlay, session-history file or prior independent record review.
The old BacDive URL redirects to the survivor; the old GOLD label URL tracks
its rename. Neither should be deleted as a supposed duplicate record.

The research report is a lead, not independent evidence for every assertion.
Its universal numerical cutoffs, subtree extrapolations and proposed xrefs
were not imported. An attempted Lake Meyghan publisher retrieval failed at
authentication redirect; its full text was not used as verified evidence.
Empty optional parameters/graphs remain appropriate. iModulonDB is
inapplicable without a gene, regulator or expression assertion.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | Three saline-only names are asserted as exact synonyms of a saline-or-alkaline environment, dropping the alkaline-only arm. | curation/term_requests.tsv:43 exact_synonym; definition application in src/habitatmech/seed.py and generated ENVO proposal. |

Counts: zero blockers, one major, zero minor. The verified genus, explicit
source merge, count/unit separation, taxonomy projection and genuine
review/history state should be preserved.

## Recommended Edits

1. Remove those three strings from the authored exact_synonym list, retaining
   the source label and full disjunctive definition. A weaker related/narrow
   representation needs an explicit maintained input; the current definition
   TSV supplies exact synonyms only. Do not hand-edit generated YAML.
2. Add regressions for all three non-equivalent aliases, the retained source
   name and both source contributions. Append required new history without
   changing old reports/events. Recover original strain/study provenance
   before any broader ecological endorsement or association deletion.
3. Preserve REPLACE/ENVO:01000317, the intentional partial-PATO omission,
   separate counts, all 25 taxon dictionaries and the two redirects. Incoming
   qualifier/material edges are separate curation questions, not a reason
   to restore the old biome ancestry or rewrite this definition.

## Follow-up Checks

After a maintained-input correction run `just seed`, then
`just seed-canary habitatmech:GOLD.ce244e62cd --force`. Inspect the whole
survivor, synonyms, both attestations, all taxa/status/history and redirects
before `just seed-apply --force`. Never prune partial runs. Require ordinary,
strict and product validation, term-request checks, new history, exact
reproduction and full QC. These are future commands, not executed edits.

The complete page exposes all aliases and all 25 source-associated taxa.
Actual in-memory removal of the three names changes semantic text; a repair
therefore needs genuine map/site refresh under #1217. Scope-only changes can
be text-neutral, so inspect the chosen fix rather than assume. Preserve
protected #1218/runtime pins and inspect actual SSSOM/KGX before compatibility
claims. This review changes no scientific input or generated artifact.

## Additional Notes

All-state exact-key and saline/synonym issue searches found no dedicated
scope correction. Closed #213 removed punctuation/coined duplicates; its
full body/comment does not address these three real but narrower names.
Open #1249 concerns ontology synonym-scope loss, not this authored row;
its full body was read. Track the bounded curated-synonym finding separately.
The historical #185 body supports preserving the completed parent/merge fix.

A source-search invocation initially named a nonexistent curation.py; it
was corrected to the actual curate/ directory and rerun successfully.
Official typed ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No old report/history, paid research, outbound contact or scientific file changed.
