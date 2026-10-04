# YAML Record Review: B-lymphocyte cell line

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/b_lymphocyte_cell_line.yaml`
- Started UTC: 2026-10-04T09:42:55Z
- Finished UTC: 2026-10-04T09:51:12Z
- Verdict: needs curation

## Target

The complete generated HabitatRecord was read: `BTO:0001522`, B-lymphocyte
cell line, HOST_ASSOCIATED, EXACT, SEEDED. It contains five PREGO related
synonyms, one source attestation, one taxon association and one seeding event.
Definition, parents, xrefs, parameters, evidence, graphs, discussions, datasets
and replacement claims are absent. This is not the separately reviewed
normal B-lymphocyte record (`BTO:0000776`).

The actual `mint("PREGO", "BTO:0001522")` function yields
`habitatmech:PREGO.716be113a9`. `data/habitats/PATHS.tsv:281` pins the stem.
Generated YAML is not a maintained curation surface.

## Validation

- `just validate data/habitats/host_associated/b_lymphocyte_cell_line.yaml`:
  PASS, no issues.
- `just validate-strict data/habitats/host_associated/b_lymphocyte_cell_line.yaml`:
  PASS, one file, zero errors.
- `just validate-products`: PASS, 1,179 canonical pairs, one synonym pair,
  five configured exceptions and 2,054 no-adapter skips. NCBITaxon is outside
  this configured gate; the displayed strain was verified separately.
- `just worklist --status all --limit 5`: PASS; 953 ungrounded records and
  1,810 decisions. This self-grounded PREGO source is not an ungrounded item.
- `just qc` is running at report completion. Lint, documentation and raw-data
  provenance have passed; tests and subsequent full-corpus/history/site gates
  have not yet produced a terminal result. Log:
  `/private/tmp/habitatmech-b-cell-line-qc-20261004.log`. No narrower reference
  or corpus validator was invented. Terminal results belong in the PR receipt.
- A read-only comparison using `build_context` and the actual `semantic_text`
  adapter confirms that removing the taxon changes semantic text. No removal
  or scientific-input edit was performed.

## Identity and Grounding

The [current official BTO term](https://www.ebi.ac.uk/ols4/ontologies/bto/classes?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FBTO_0001522)
is active, with the same canonical label and no definition or replacement.
The structured `ontology_terms.tsv:1522` row has an empty deprecated field;
`TRUE` belongs to `directly_referenced`, not deprecated. The initial visual
column misreading was corrected against the header and current OLS before
forming a finding. There is no supported obsolescence issue.

OLS reports zero direct subclass parents. Its typed graph instead connects
this cell-line class to B-lymphocyte by `RO:0002202`, develops from. The seven
vendored subclass edges involving the target have it as object, not subject:
they name child lines, not parents. The empty generated parent list therefore
agrees with the inspected subclass source. Do not convert the develops-from
edge into a strictly-broader habitat assertion.

`ingest_prego` supplies the self-grounded EXACT route. No item decision was
found for the actual source key in ignored-inclusive searches; SEEDED and the
single 2026-08-16 event are consistent. An absent mapping predicate is correct
when the source ID is the record identity. HOST_ASSOCIATED describes the cell
site, not a whole-host taxon equivalence. The literature below demonstrates
that a B-cell line can host viable intracellular bacteria under specified
conditions, so the concept is not automatically NOT_APPLICABLE.

## Evidence

`data/raw/prego_habitats.tsv:602` contains one taxon, one direct assertion,
score 3 and `annotated_genomes_isolates`. The emitted TAXON count, score and
channel match. `prego_habitat_taxa.tsv:2381` contains the sole ranked pair:
`NCBITaxon:375177`, Haemophilus influenzae 3655, score 3, direct TRUE, no
corroboration. Rank 1 and candidate_pool 1 match and involve no top-25
truncation. This is neither prevalence nor a characteristic-taxon assertion.

Fresh [NCBI taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=375177)
efetch confirms the ID, scientific name and strain rank. The five PREGO
synonyms exactly retain the noncanonical raw aliases as RELATED_SYNONYM,
including the awkward `linous` forms. They are source-provided search aliases,
not preferred scientific names or unsupported exact ontology synonyms. Current
BTO's flat `B-cell line` synonym does not authorize rewriting PREGO scope.

Three original papers were inspected via official Europe PMC full-text XML,
including their PMID/DOI identifiers and the relevant text:

- [PREGO methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC8879827/),
  PMID:35208748, DOI:10.3390/microorganisms10020293, section 2.3: the
  annotated-genomes channel includes taxon associations text-mined from
  BioProject-linked abstracts and assigned confidence 3. Channel and direct
  flag alone do not establish localization in the named cell line.
- [Comparative Haemophilus genomics](https://pmc.ncbi.nlm.nih.gov/articles/PMC3928620/),
  PMID:24438474, DOI:10.1186/1471-2164-15-38, Table 1: strain 3655 is listed
  as nontypeable, from the middle ear of a child with acute otitis media in
  Missouri. This inspected strain context does not establish B-cell-line
  occurrence. It is not claimed as the original PREGO citation, nor does a
  middle-ear origin prove the strain cannot occur in another site.
- [Selective Salmonella infection](https://pmc.ncbi.nlm.nih.gov/articles/PMC3510171/),
  PMID:23209805, DOI:10.1371/journal.pone.0050667, cell-culture/plating
  methods and Figure 2: microscopy and viable recovery after extracellular
  killing demonstrate intracellular replication in Ramos cells. Primary B
  cells behave differently. This supports a bounded cell-line habitat, not
  the displayed Haemophilus pair or all cell lines; no Salmonella was added.

The original PREGO pair citation remains unrecovered. Ignored-inclusive
`find` of the configured upstream `data/` and `kg_microbe/` trees found no
PREGO payload. The official manifest-pinned transform was freshly inspected:
it emits BTO location_of taxon and retains evidence_url. HabitatMech's
`extract_prego` drops that URL while retaining scores/channel/rank. The
association therefore cannot be resolved from the retained inventory alone.

## Completeness

All 14 raw TSV inventories were parsed, including extra-column values, for
the exact ID, mint and cell-line label variants. Only the PREGO aggregate and
single taxon belong to the exact target. Ontology hits for distinct pre-B,
pro-B and named cell lines were not merged. No target BacDive, Madin, GOLD
tree/bulk/study/triad, parameter or isolation-grounding row was found.

Ignored-inclusive searches of curation, history, research, reports and
RETIRED found no target decision, definition request, graph overlay, research
report, retirement or previous individual review. No governed association-
qualification input was found in curation, implementation, config or scripts.
Empty optional fields are not independently defects. This record asserts no
gene, regulator, locus or expression dataset; iModulonDB is not applicable.

## Findings

- **Major (1): cell-line occurrence scope of the exact PREGO strain pair is
  unresolved.** Retained provenance establishes an association, not whether
  it is localization, immune response, disease context, protein assay or
  background mention. The maintained owners are the upstream exact-pair
  assertion and `src/habitatmech/extract.py::extract_prego` / the governed
  association contract consumed by `src/habitatmech/seed.py::ingest_prego`.
  Tracked in [#1369](https://github.com/CultureBotAI/HabitatMech/issues/1369).
- Blockers: 0. Minors: 0. No identifier, copied-count, rank or current label
  mismatch was found; no unsupported biological-absence claim is made.

## Recommended Edits

1. Recover the manifest-matching pair and original citation, then qualify
   its precise biological relationship. Do not automatically remove the taxon.
2. Preserve pair evidence in maintained extraction inputs; use a governed
   pair-qualification mechanism or correct the upstream assertion when
   warranted. Keep raw source totals separate from any qualified pool. Do not
   use an identity decision as an undocumented taxon filter.
3. Keep the valid cell-line identity, weaker PREGO aliases and missing
   subclass parent unless separately supported evidence warrants changes.
   Coordinate shared evidence retention with #1367, #1314 and #1321, which
   concern other exact pairs, rather than pretending those records are this one.

## Follow-up Checks

Test original-source retention, localization versus background/assay mentions,
and stable raw/qualified count semantics. Append history for actual curation
changes; dry-run/canary/reseed and re-read the record. Run strict validation,
current taxonomy checks, OAK, provenance, history, `just verify-corpus`, site
checks and full `just qc`.

The full-context adapter diagnostic removes `observed taxon: Haemophilus
influenzae 3655` when that entry is removed. Any evidence-supported removal
therefore needs real map/site regeneration; #1217 documents the supported-
runtime constraint. Evidence-only changes may be text-neutral and should be
compared rather than assumed. Never fake generated hashes or relax freshness.

## Additional Notes

The inventory manifest pins kg-microbe
`7698351a54b48f2e917635fdf51cd0a6b323135d`, extracted 2026-08-16T05:58:02Z.
Inspected [transform](https://github.com/Knowledge-Graph-Hub/kg-microbe/blob/7698351a54b48f2e917635fdf51cd0a6b323135d/kg_microbe/transform_utils/prego/prego.py#L874-L888)
retains the evidence URL at lines 930/1002; the local loss point is
`extract.py:331-429`.

Broad numeric literature searches returned unrelated 3655 matches and were
not treated as evidence. Haemophilus-constrained Europe PMC searches returned
31 strain/B-cell-related hits and 71 species/B-cell-line hits; the first 25
metadata leads of each were screened, not all literature. The laminin paper
PMC7368242 was only a lead: full-text XML returned HTTP 500 twice and PMC
HTML returned a browser challenge, so its snippet was not used as evidence.
All 512 returned open/closed issue bodies were searched for the exact target
and strain before filing #1369. Only this new report was written in the repo;
no scientific inputs, generated records or curation status were changed.
