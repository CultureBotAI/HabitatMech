# PR Review: Xeric Basin Biome

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1606
- Baseline: `1c066989c30b8bd885361fe836de49d8cc71a36c`
- Reviewed report commit: `ecbb86ffef8a8a44462175eeb92432527778357a`
- Reviewer: Codex, separate adversarial pass; no independent-agent approval claimed.

## Scope and Method

Publish the completed individual xeric-basin review unchanged. The unfinished
Biopsy investigation is excluded. Read the full report and generated record,
the complete proposed diff, relevant raw PREGO rows, the extractor's ranking
and label-loading paths, semantic-text implementation and repository publication
contracts. Challenge aquatic identity, source versus ontology synonyms,
count/score/rank interpretation, taxon naming, evidence limits and scope creep.

Fresh official typed ENVO at revision
`a2455d1a77e46bb8a664d65a157166b539269042` (106,817 triples) confirms active
ENVO:00000893, its exact label/definition, no typed synonyms and sole named
parent ENVO:00000873 freshwater biome. Fresh inspection of that parent and
ENVO:00002030 verifies the aquatic hierarchy. The spring-abundance comparison
remains an explicitly unresolved precision question, not an established error
or permission to override an ontology-owned definition.

Fresh official NCBI Taxonomy EFetch resolves all 25 IDs directly, with no
merged aliases: 17 species, seven strains and one no-rank group. All 23 supplied
names match. The two absent names are the same minor finding recorded in the
individual report; validity of identifiers does not validate habitat occurrence.

## Findings and Disposition

No additional blocking defect in the report-only diff was established.
The existing minor scientific finding remains unresolved:

- Rank 16, NCBITaxon:36987: Coptotermes formosanus.
- Rank 18, NCBITaxon:39946: Oryza sativa Indica Group.

Added this target's evidence and acceptance criteria to the existing root-cause
issue [#1257](https://github.com/CultureBotAI/HabitatMech/issues/1257#issuecomment-6029509630),
after reading its body and comments. A duplicate issue was not created. Keep
the issue open: this PR does not implement a taxonomy repair. The original
review's statement that the issue did not yet track this target is historical;
the publication comment now supplies that link.

An ignored-inclusive filename search across `build` and the configured
kg-microbe data directory found no PREGO nodes/edges or NCBITaxon source-node
dump. Explicit checks also confirm that the three configured input files do
not exist. This is a bounded source-availability blocker for governed
re-extraction, not proof that the underlying associations are false. Filling
generated YAML or changing raw bytes/checksums alone would bypass source
provenance. No such edit was made.

A future versioned-source repair must preserve the target's 36-TAXON pool,
36 direct source assertions, 25 retained IDs/ranks, tied score-4 observations,
environmental_samples channel and SEEDED state. It must not borrow the lake
alias case or discard nonmicrobial observations solely because of lineage.
An actual in-memory `semantic_text` probe confirms that adding the two names
adds two observed-taxon lines. Therefore source refresh, applicable session
history, canary/full reproduction and genuine semantic-map/site regeneration
are necessary for the repair. The probe wrote no data.

## Preservation and Validation

Fresh full-corpus construction reproduces every field of the target: one
source concept, zero reviewed sources, 25 taxa and one event. The complete
scientific/product diff against the baseline is empty: no changes under
`src`, `scripts`, `curation`, `data`, `pages`, `history` or `conf`, nor to
README or justfile. Report publication does not require fabricated regenerated
products, a new curation event or a change to mapping status.

Fresh local `just qc` is running at audit creation. Initial-head CI label
correspondence and vendored sync have passed; QC is pending. Final-head and
exact merge-candidate checks remain required, with final receipts to be posted
on the PR before completion. No admin bypass or self-approval is used.
No browser visual QA, original PREGO re-extraction or new SSSOM/KGX readiness
assessment was performed.

Ignored-inclusive `Path.rglob` census: 1,075 reports cover 1,074 distinct
current records; 2,132 of 3,206 remain, with no unparsed reports. The all-record
review goal is unfinished.
