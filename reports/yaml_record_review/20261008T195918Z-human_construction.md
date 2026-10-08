# YAML Record Review: human construction

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/human_construction.yaml`
- Started UTC: 2026-10-08T19:56:13Z
- Finished UTC: 2026-10-08T19:59:18Z
- Verdict: pass (0 blocker, 0 major, 0 minor)

## Target

Read the complete generated HabitatRecord ENVO:00000070 at
`55b6ab62ae8585358b44db80e681000a02ebb3ec`. ENGINEERED / EXACT / SEEDED;
one ENVO definition, three source-qualified synonym assertions, two parents,
one PREGO attestation, 25 displayed taxa and one generated seed event.
The referent is the assembled material construction, not the construction
process, human host, indoor air or every sample collected inside a building.

## Validation

Fresh `UV_CACHE_DIR=build/uv-cache just validate` and `just validate-strict`
on this exact path passed: no open-schema issues and zero strict errors.
Fresh `build_corpus` / `build_document` reproduces the complete parsed
target, with one contributor, zero ITEM-reviewed contributors, both parents
and no applied authored definition or GOLD exclusion.

The immediately preceding unchanged-baseline checks in this review session
passed: `just verify-corpus`, all 3,208 records with zero differences;
`just validate-history`, all 201 receipts; `just provenance-check`, all
14 inventories and two GOLD sources. Guidance, code, inputs, tests and
generated records are unchanged from c6c94db6f. Its full local QC receipt
records 597 passing tests, three skips and all gates passed; full QC was not
rerun for these report-only edits. Prior label correspondence does not prove
taxon ecology or synonym scope. Direct ENVO/NCBI checks below supplement it.
No target graph or literature collection requires a focused validator.

Original PREGO assertion/sample joins were not verified. The live portal
was unavailable to the web reader; this is not evidence that the service or
its data no longer exist. No CI, SSSOM/KGX or whole-corpus scientific
approval is claimed.

## Identity and Grounding

`PATHS.tsv:468` agrees with the ID and slug. The recomputed source key is
`habitatmech:PREGO.7aa287b1e4`; no target decision was found. Inspected
`ingest_prego` uses `prego_self_grounded`, preserving the explicit source
ontology ID as EXACT rather than making a lexical cross-source merge.
Zero ITEM decisions explains SEEDED. An absent mapping predicate is valid
because the record is the source concept, not a distinct mapped target.
Category inference follows the ENVO construction ancestry.

Fresh [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
confirms the definition, exact synonym `constructed feature`, and both
named superclasses: ENVO:01001813 construction and ENVO:01000813
astronomical body part. The construction parent permits assembly by
organisms or machines, so human-built constructions are narrower. The
astronomical-body placement is an explicit ENVO axiom, not a newly inferred
GOLD containment edge. No specific contradictory target case was found.

All three classes lack a deprecation assertion in the inspected OWL.
An editorial comment suggesting future restructuring is not owl:deprecated.
The ontology's part-of-technosphere and construction-process restrictions
are not incorrectly emitted as strictly broader habitat IDs. The two
external parents occur in the ontology slice but not PATHS; they need not
have generated corpus pages to be valid references.

The two PREGO aliases remain RELATED_SYNONYM, including the plural spelling.
The same singular text can correctly have an independent ENVO exact scope.
Unlike Household waste material, this inspected ontology alias is actually
typed exact. The generated attestation label comes from the ontology label;
the PREGO nodes lack their own canonical label and retain their source
spellings in prego_synonyms. This is not proof of an independent label source.

## Evidence

- `prego_habitats.tsv:111` supplies 376 distinct taxa, 376 direct source
  assertions, maximum score 1.52439, only environmental_samples, and the
  two source aliases. TAXON does not count buildings, samples or studies.
- `prego_habitat_taxa.tsv:3611-3635` supplies all 25 displayed IDs, labels,
  ranks and scores, ranging from 1.52439 to 1.30642. Every retained row has
  source direct=TRUE, environmental_samples and no corroborating source.
  That direct flag is an upstream edge property, not proof of strain isolation
  or a controlled colonization experiment. The 376-member candidate pool
  makes the top-25 truncation explicit; the record is not a complete census.
- `ontology_terms.tsv` logical row 6658 (physical line 6664) supplies the
  identity fields; `ontology_subclass_edges.tsv:4701-4702` supplies the two
  parents. Additional incoming child edges were identified but not reviewed
  as separate records.
- Fresh [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=798130,1218948,160488,216591,176299,216595,381754,287,482957,228410,390235,661410,208963,648,269482,272942,272630,395019,746360,441620,31998,440085,100226,562,350702&retmode=xml)
  resolves all 25 IDs with exactly matching current scientific names:
  20 strain-rank and five species-rank entries. PF5, KT2440 and bracketed
  Pseudomonas [fluorescens] SBW25 are retained as returned, not silently
  reassigned to a similarly named strain. Taxonomic identity does not
  validate the environmental association.
- The inspected primary [PREGO methods paper](https://imbbc.hcmr.gr/wp-content/uploads/2022/03/2022-Zafeiropoulos-Micro-12.pdf),
  DOI:10.3390/microorganisms10020293, sections 2.1 and 2.4, describes
  environmental-sample associations from taxonomic profiles and tagged
  sample metadata, scored on a (0, 5] scale. This supports interpretation
  as ranked associations, not probabilities, prevalence, abundance or
  independent isolate observations. It does not validate these particular
  25 pairs or recover their original sample identifiers.

The record has no is_characteristic, causal mechanism, growth condition or
independent corroboration claim. Generic construction ecology must not be
used to strengthen those absent claims.

## Completeness

Ignored-inclusive searches covered the ID, minted source key, label,
constructed-feature aliases and stem in curation, raw inventories,
PATHS/RETIRED, configuration, docs, tests, histories, research and reports.
Related Monument/cooling-tower definitions and construction-context research
were found; they are not target-owned decisions, evidence dossiers or
independent support for the 376 associations. No target-owned authored
definition, overlay, exclusion, session receipt or prior individual review
was found in those bounds.

A complete CSV exact-field/pipe-member traversal of all raw TSVs found the
PREGO aggregate, all 25 taxon rows and ontology metadata/edges. No direct
additional-source attestation, target environmental-parameter or triad row
was found. Ignored-inclusive `find` under build, data/raw and the configured
kg-microbe data directory found no files within a PREGO source directory.
The manifest records the original transformed nodes and edges, including
their sizes and hashes, but those receipts cannot substitute for source joins.

Empty mechanism, conditions, discussion and dataset slots should stay empty
without target evidence. iModulonDB is not applicable: the listed strains
carry occurrence associations, not gene, regulator or expression claims.

## Findings

None found: zero blockers, zero major findings, zero minor findings.
The pass covers identity, faithful inventory-backed representation and
appropriately limited claims, not validation of every source association
or an ITEM-reviewed scientific endorsement of the whole class.

## Recommended Edits

No immediate correction is established. Preserve the ontology identity,
actual exact alias, independent PREGO related aliases, source score/channel,
TAXON units, explicit candidate pool and SEEDED status. A future ITEM review
belongs in `curation/decisions.tsv` under the PREGO source mint; it must not
upgrade association strength without source-level evidence. Any demonstrated
pair-level defect belongs in upstream PREGO evidence/import handling, not
an invented whole-record grounding change.

## Follow-up Checks

Recover manifest-bound PREGO edges and supporting sample metadata to audit
the 376-pair cohort, distinguishing structural material, surface, sampled
fluid and mere location. Verify strain resolution separately from habitat
co-occurrence. Recheck named and relational ENVO axioms after ontology
refreshes. If curation is authorized, inspect a canary and pass strict,
history, provenance, label, exact-corpus, map/site and full QC checks.

## Additional Notes

Only this new target report was written. No scientific/generated input,
prior report, history, lifecycle status or GitHub item was changed. No paid
research or delegation. Fresh primary bytes were parsed in memory:

- ENVO: 9,614,229 bytes, SHA256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- NCBI: 86,890 bytes, SHA256
  `07107fa7f89a60efbaed82e0929e461366b5747c5653853f22f488c3549441d1`.
