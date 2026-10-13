# YAML Record Review: crustacean-associated environment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/arthropoda_crustaceans.yaml`
- Started UTC: 2026-10-04T05:54:46Z
- Finished UTC: 2026-10-04T06:02:24Z
- Verdict: pass

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.2959225799`:
HOST_ASSOCIATED, UNGROUNDED, REVIEWED. It contains a curated definition,
one source-label synonym, two broader environment parents, one GOLD
attestation with 598 ORGANISM assertions, and three generated events.
The actual `mint` helper reproduces its identifier from Host-associated >
Arthropoda: Crustaceans. `data/habitats/PATHS.tsv:1591` preserves its
source-label filename.

## Validation

- `just validate data/habitats/host_associated/arthropoda_crustaceans.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/arthropoda_crustaceans.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh local `just qc` passed lint, documentation and raw provenance and
  remains in tests at report completion. No terminal local QC or fresh local
  corpus-reproduction result is claimed here. This command includes history,
  strict schema, corpus reproduction, reference/invariant tests, generated-site,
  redirect and term-request checks.
- Exact unchanged base `aca0c1c1c828ca77d4f492a9678e08518c26eeb6` has successful
  [QC 37181085661](https://github.com/CultureBotAI/HabitatMech/actions/runs/37181085661).
  The merge-group QC for that base also passed all 457 tests, with three skips
  and two warnings. These are baseline results, not this report's final-head CI.
- Current official OLS term JSON and primary PubMed EFetch XML were inspected.
  A PMC browser challenge did not prevent reading the two PubMed abstracts;
  no successful full-text inspection of those papers is claimed.

## Identity and Grounding

`curation/decisions.tsv:323` is ITEM CONFIRM_UNGROUNDED with the animal-associated
environment as a parent. `curation/term_requests.tsv:10` supplies the authored
label, definition, exact source-label synonym and ADD-mode genus. The
August 12 decision and August 16 definition/seed events match those inputs.
REVIEWED follows the sole contributing source concept's ITEM depth.

Vendored ontology rows 8495/8497 and current non-obsolete
[ENVO:01001000](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001000)
and [ENVO:01001002](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001002)
agree on the organism-determined and animal-associated environment meanings.
Subclass row 6797 places the latter beneath the former. The GOLD Host-associated
ancestor and the curated animal-associated genus are both genuinely broader.
Retaining the true ancestor with ADD is not a false parent or an identity merge.
Both complete local parent records were read; their counts, taxa and parameters
are not inherited by this target.

The live, non-obsolete
[ENVO:01001176](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001176)
requires an aquatic-invertebrate context and is neither an exact replacement
nor a safe superclass for a source bin that does not require aquatic hosts.
The current ENVO search for crustacean associated environment returned zero
results; ignored-inclusive searches of the vendored ontology slice found no
matching class. These are bounded search results, not proof that every possible
ontology synonym has been exhausted. A host taxon, an anatomical compartment,
processed seafood and aquaculture water are not substitute identities.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:62` supplies the exact depth-two source path,
nodes 7210, 7211, 7212 and 7213, 598 organisms, and zero study/biosample
assertions. First-node ID, four-node note, source label/path, count and unit
are faithful to that inventory. The 598 is a source assertion count, not
microbial species richness, prevalence or a current census of GOLD.

Full structured scans covered 2,562 tree paths, 1,040 bulk biosample rows,
4,587 studies and 1,587 triads. Crustacean wording matched 53 tree paths,
10 bulk rows, 21 studies and 12 triads. Exact-path comparison, including
membership in the studies' pipe-delimited path lists, found no target path
in those three side tables. The tree matches comprise 47 host-branch paths
including the target and six engineered aquaculture paths. Child-compartment
and aquaculture counts must not be pooled into this record's 598.

The committed crustacean definition-research report was read as a lead,
not independent support for its broad ecological or numerical statements.
Inspected primary [Wang et al. 2004](https://pubmed.ncbi.nlm.nih.gov/15466563/)
abstract and identifier metadata verify DOI:10.1128/AEM.70.10.6166-6172.2004
and PMC522098. The abstract explicitly identifies Porcellio scaber as a
terrestrial isopod crustacean and reports bacterial colonization of its
midgut glands, supported by FISH and microscopy. The inspected
[Collingro et al. 2015](https://pubmed.ncbi.nlm.nih.gov/26272556/)
abstract and metadata verify DOI:10.1128/genomeA.00674-15 and PMC4536667,
describing a bacterial symbiont in that terrestrial host's hepatopancreas.
These bounded observations support rejecting an aquatic-only restriction;
they do not establish a universal crustacean microbiome, GOLD sample identity
or a mechanism for this whole habitat class. No paper-derived taxa or counts
are copied into the record.

## Completeness

Ignored-inclusive identifier/label/stem searches covered curation, history,
research, prior review reports, raw inventories, PATHS and RETIRED. They found
the maintained decision/definition, generated ENVO template at row 16,
research report and label-change redirect at RETIRED row 27, but no prior
exact-target review, causal overlay or target-specific session history.
The nauplius session references this parent; it is not a crustacean-target
session. Older curation does not require a new session for a read-only audit.

Full structured scans of the other eight source tables covered 162 BacDive
sources, 3,081 BacDive taxa, 770 parameters, 358 mappings, 58 Madin habitats,
1,378 Madin taxa, 719 PREGO habitats and 8,807 PREGO taxa. No target-key or
crustacean-word match was found; this does not exclude evidence under individual
host names. The definition rationale's general mention of BacDive organization
does not create a BacDive attestation for this particular record.

Optional xrefs, parameters, characteristic taxa, evidence, mechanisms,
discussions and datasets can remain absent. iModulonDB is not applicable:
the record makes no gene, regulator or expression claim.

## Findings

None found: zero blocker, major or minor findings established for this target.
No unsupported identity, parent, count or causal assertion was found.

## Recommended Edits

None. Preserve the minted host-environment identity, source scope and count,
both broader parents and the existing term request. Future identity/grounding
changes belong in `curation/decisions.tsv`; definition/genus changes belong in
`curation/term_requests.tsv`. Do not patch generated YAML or pages.

## Follow-up Checks

Require terminal local QC and the PR's required final-head/merge-queue checks
before publication. Any future ontology grounding change needs an inspected
exact match, a guarded canary, strict validation, OAK correspondence, corpus
reproduction, site/map freshness and full QC. External ENVO submission still
requires explicit per-request approval; this report does not submit one.

## Additional Notes

Searched all 502 existing issue titles, bodies and returned comments for the
target key, label and crustacean wording, then inspected all four matches.
Open #320 and #321 concern separate post-larval/zoeal records; open #1331
concerns a hindgut compartment's false whole-hindgut superclass; closed #1335
corrected another report's source-attribution wording. None establishes a
defect in this clade-level target, so no duplicate or speculative issue is
recommended. This review is not an independent PR approval.

No generated record, decision, definition, status, curation event or session
history was changed. Parent/reference reads do not add review coverage.
No paid research ran. Whole-corpus review remains ongoing.
