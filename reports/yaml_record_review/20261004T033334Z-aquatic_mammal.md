# YAML Record Review: aquatic mammal-associated environment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/aquatic_mammal.yaml`
- Started UTC: 2026-10-04T03:29:22Z
- Finished UTC: 2026-10-04T03:33:34Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `habitatmech:BACDIVE.15180e7ff9`:
HOST_ASSOCIATED, UNGROUNDED, REVIEWED. It has an authored definition, one
curated source synonym, one environment parent, one organism xref, one
BacDive attestation, 25 observed-taxon entries and three curation events.
Actual `mint` reproduces the source key; `PATHS.tsv:1171` pins the filename.

## Validation

- `just validate data/habitats/host_associated/aquatic_mammal.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/aquatic_mammal.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch `just qc` remains in tests; lint, documentation and raw
  provenance passed. No terminal success is claimed yet.
- All 25 taxon IDs/names were checked against current NCBI taxonomy EFetch;
  all resolve directly and labels agree. A separate field comparison confirms
  all 25 generated source/count/rank/pool values match their inventory rows.
- Current official OLS and primary PubMed EFetch requests succeeded.
  Browser PubMed retrieval failed for two leads; direct abstracts supplied
  the actual evidence. BacDive's strain page and isolation section worked.

## Identity and Grounding

`curation/decisions.tsv:1536` is ITEM CONFIRM_UNGROUNDED with HOST_ASSOCIATED
category and an xref to FOODON:03411134. `curation/term_requests.tsv:54`
provides the current definition, label, synonym and ADD parent. The August
16 decision/seed and August 28 definition events faithfully reflect these
inputs. An associated environment remains distinct from the mammal organism.

Current non-obsolete [ENVO:01001002](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001002)
matches vendored row 8497: animal-associated environment, determined by an
animal. Current non-obsolete [FOODON:03411134](https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON%3A03411134)
matches row 10682 and denotes mammal, not its environment. The organism
xref is allowed by the local host rule; it is not the habitat identity.

Ignored-inclusive searches of the complete vendored term table and bounded
current OLS ENVO queries for aquatic mammal and mammal-associated found no
exact environment identity. Returned keyword near-misses do not justify
grounding. These checks do not prove absence from every ontology.

The definition is not yet a resolved description of the source extension.
The ITEM note explicitly interprets the genus as a living animal host, while
the source also contains carcass-adjacent sediment isolates. The current
sentence lacks an explicit resolution of that distinction. This finding
does not claim that ENVO:01001002's short definition alone proves an
absolute living-only constraint.

## Evidence

`bacdive_isolation_sources.tsv:82` supplies 69 STRAIN assertions and a
46-taxon pool. `bacdive_source_taxa.tsv:164-188` supplies the retained top
25, with counts, ranks and labels reproduced exactly; no corroboration or
is_characteristic flag is added. The retained list is not all 46 taxa and
counts are not prevalence, patients or independent studies.

`isolation_source_groundings.tsv:26` records upstream closeMatch to mammal;
the ITEM decision deliberately retains it as an organism xref.
`src/habitatmech/extract.py:241-327` explains the source/strain/taxon join
and top-25 retention; `seed.py:915-1010` explains the generated fields.
Taxonomy validity does not establish the anatomical isolation context.

The complete committed aquatic-mammal research report was read, including
its source caveat, alternatives and near-miss table. It explicitly warns
that six retained taxa came from whale-fall sediment and requires a curator
to resolve that boundary. Its older OTHER-category complaint is already
superseded by the current category; it is not a new finding.

Three primary abstracts independently verify the six exact strain aliases:

| Retained NCBITaxon | Strain alias | Verified primary source |
| --- | --- | --- |
| 1122599 | Neptunomonas japonica DSM 18939 = JAMM 0745 | [PMID:18398184](https://pubmed.ncbi.nlm.nih.gov/18398184/), DOI:10.1099/ijs.0.65509-0 |
| 1278303 | Psychromonas macrocephali ATCC BAA-1527 = JAMM 0415 | [PMID:18599721](https://pubmed.ncbi.nlm.nih.gov/18599721/), DOI:10.1099/ijs.0.65744-0 |
| 1278307 | Psychromonas ossibalaenae ATCC BAA-1528 = JAMM 0738 | same Psychromonas paper |
| 1278312 | Psychromonas aquimarina ATCC BAA-1526 = JAMM 0404 | same Psychromonas paper |
| 1278309 | Amphritea japonica ATCC BAA-1530 = JAMM 1866 | [PMID:19060065](https://pubmed.ncbi.nlm.nih.gov/19060065/), DOI:10.1099/ijs.0.65826-0 |
| 1278310 | Amphritea balenae ATCC BAA-1529 = JAMM 1525 | same Amphritea paper |

Primary ArticleIdList entries verify each PMID/DOI pair; NCBI strain aliases
agree. All three papers state isolation from sediment adjacent to sperm-
whale carcasses. These are six exact strain witnesses, not proof that their
species can never occur in a living host.

The inspected [BacDive 134369 record](https://bacdive.dsmz.de/strain/134369)
independently connects taxon 1278310 to ATCC BAA-1529/JAMM 1525 and sediment
isolation. Its source categories include both decomposing animal and aquatic
mammal. This is positive source evidence of the mixed extension, not a
conclusion drawn only from species names or generated research prose.

The primary [Bik et al. 2016 abstract](https://pubmed.ncbi.nlm.nih.gov/26839246/)
supports genuine host-associated microbial communities in sampled dolphins
and sea lions distinct from adjacent seawater. ArticleIdList verifies
DOI:10.1038/ncomms10516 and PMC4742810. It neither reclassifies sediment
strains as host isolates nor supplies observations for all aquatic-mammal
lineages. No abundance, phenotype, prediction or causal mechanism is imported.

Current [ENVO:01000140](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000140)
denotes the fallen whale carcass; adjacent sediment is not automatically
that identity. [ENVO:01001055](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001055)
explicitly scopes an animal part or small animal. The research report's
suggested broader alternatives therefore still require relation-level
review, rather than automatic adoption as a whole-whale genus.

## Completeness

Ignored-inclusive source key, label and filename searches covered curation,
history, research, prior reviews, raw inputs, PATHS and RETIRED. They found
the decision, definition, generated term request, research report and two
retired aliases, but no target overlay, session or earlier exact-target
review. Old decisions do not retroactively need a later-style session merely
for review. The research manifest records two failed attempts and a later
successful report; no paid run was repeated.

Complete scans of all raw source tables found the BacDive source, its 25
taxon rows and its mapping. Under the target key/aquatic-mammal wording,
there were no matches in 770 parameter rows, 2,562 GOLD paths, 1,040 bulk
rows, 4,587 studies, 1,587 triads, 58 Madin habitats, 1,378 Madin taxa,
719 PREGO habitats or 8,807 PREGO taxa. This does not exclude other habitats
containing the same taxa. Optional fields are not quotas. iModulonDB is not
applicable: no microbial gene or expression-module claim is being assessed.

## Findings

1. **Major - HM-AQUATIC-MAMMAL-001:** the curated host interpretation does
   not reconcile six supported carcass-adjacent sediment associations, despite
   its own research caveat. Owners: `curation/decisions.tsv:1536`,
   `curation/term_requests.tsv:54`, and source association handling in
   `src/habitatmech/extract.py:241-327` / `seed.py:915-1010` or a governed
   association-level input. Filed as
   [#1340](https://github.com/CultureBotAI/HabitatMech/issues/1340).

No blocker or minor finding established. Current IDs, field derivation,
minted identity, organism-xref handling and observational flags are sound.

## Recommended Edits

Decide explicitly whether the retained concept is a broad source bin or a
living-host environment. Preserve raw BacDive evidence; qualify or separate
the exact sediment associations through maintained inputs when choosing the
latter. Keep source totals distinct from filtered pools. Do not simply drop
six raw assertions, invent a replacement genus, narrow aquatic to marine,
ground to a mammal taxon or globally ban these species from host records.

A read-only real-adapter comparison confirms excluding the six entries
changes semantic input. Append required history, inspect a guarded canary
and regenerate map/site with supported tooling under #1217. Do not edit
generated YAML, stale checksums or draft #1218 to bypass regeneration.

## Follow-up Checks

Regress all six exact strain/context links plus a retained host-derived
control. Recheck all 25 taxon identities and source count/rank/pool semantics,
definition/category/genus consistency, provenance, strict schema, OAK,
history, corpus reproduction, map/site/redirect freshness and full QC.
Preserve both retired aliases if the identity or label changes.

## Additional Notes

All 493 issue bodies and returned comments were searched before #1340 was
filed. #211 concerns pinned filenames, not this evidence scope; #1215 concerns
different GOLD parents. A source-derived slug is not a new defect merely
because the authored label differs. No scientific input, generated artifact
or history changed; no paid research ran.
