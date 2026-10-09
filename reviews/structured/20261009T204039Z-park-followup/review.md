# park: verified correction at bf924eac6 and retained scope findings

- Review: 20261009T204039Z-park-followup
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-09T20:21:32Z
- Finished UTC: 2026-10-09T20:40:39Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The guarded City-context parent exclusion is verified and resolves F1/#1818. The generic ENVO genus, both source attestations and all eight historical PREGO taxa are unchanged. Urban/generic source equivalence and merged-taxonomy normalization remain open; this is not an independent scientific approval or a clean scientific pass.

## Scope And Provenance

Historical review of the entire corrected park record at retained Git revision bf924eac64712ae5e57de81b7209284ab0470dc9, with focused verification of the City-parent exclusion and retention of both unresolved predecessor findings. This assesses that exact revision, not an unspecified current working tree. All64 scientific input hashes were separately verified identical in the later product commit and current files.

Selection: Follow-up of 20261009T201157Z-park after separately authorized correction in PR1815.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base bf924eac64712ae5e57de81b7209284ab0470dc9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00000562 | data/habitats/engineered/park.yaml | generated | park |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corrected schema | passed | True | ENVO:00000562 | No issues found. |
| Corrected closed schema | passed | True | ENVO:00000562 | One file,zero errors. |
| Corrected full native QC | passed | True | ENVO:00000562 | Successful authoritative product-commit QC:650 passed,3 skipped;225 native history records,3208 closed-schema records and exact corpus reproduction,32 overlays,curation floor,site,redirects,term requests and all quality gates passed. Raw CI log inspected; no final-head result is preclaimed. |
| Fresh ontology labels | passed | True | ENVO:00000562 | 1178 canonical,1 synonym,5 exceptions,2057 no-adapter skips. |
| Trusted-base native review validation | passed | True | ENVO:00000562 | 55 bundles valid and4 contract tests passed before saving this follow-up. |
| Whole-corpus correction regression | passed | True | ENVO:00000562 | 1 passed; only park document and semantic input change; every unrelated claim and record preserved. |
| Target causal and expression-module checks | not_applicable | False | ENVO:00000562 | No target overlay or gene/expression claim. Baseline full QC validates repository-wide causal/reference constraints. |
| Original upstream membership and PREGO association evidence | unavailable | False | ENVO:00000562 | Baseline bounded source-access limitations remain; no new ecological inference is substituted for unavailable source evidence. |
| Exact corrected corpus reproduction | passed | True | ENVO:00000562 | 3208 expected/found,zero missing/extra/differing. |
| Downloaded map and vector verification | passed | True | ENVO:00000562 | Passed after artifact download completed. Input bytes match local export;3208 unique finite points,unchanged membership,only Park semantic row changed. |
| Generated site verification | passed | True | ENVO:00000562 | 3208 habitat pages,252 redirects,8 categories,114 term requests; pages in step with corpus. |
| Native session history | passed | True | ENVO:00000562 | One native history record valid. |
| Review-base publication durability | passed | True | ENVO:00000562 | 2 tests passed; separately verified published annotated tag peels exactly to bf924eac64712ae5e57de81b7209284ab0470dc9. |
| Local locked numerical runtime | failed | False | ENVO:00000562 | Locked Torch2.14.0 has no macOS x86_64 wheel. Used unchanged locked Linux runtime in successful run37986401900; no dependency workaround or pin change. |
| Initial artifact check before download completion | failed | False | ENVO:00000562 | Premature check found no current.json while artifact download was still running. Same download was awaited to terminal success; subsequent complete-artifact check C10 passed. Not a validation failure of the finished bundle. |

## Scientific And Domain Assessments

### Physical habitat and source identity

identity: supported. Targets: ENVO:00000562.

The generic ENVO park definition covers recreation/conservation areas, not only urban parks and not incorporated settlements. Current GOLD examples substantiate city-park surfaces. A primary genome paper for PREGO-listed Thermosphaera aggregans DSM11486 instead gives a Yellowstone hot-spring water/sediment origin. This supports keeping generic-park geography distinct from urban source qualification; it does not prove how PREGO generated every association.

### Exact identity, source mapping and broader scope

grounding: concern. Targets: ENVO:00000562.

PREGO self-identity is explicit. The GOLD EXACT mapping is based on the bare leaf and an ITEM REVIEW note; the City qualification and recovered urban samples make generic equivalence questionable. A supported broad mapping or retained qualified mint may be appropriate, but sample examples alone do not establish the source vocabulary's entire intended extension. The separately corrected City parent is not evidence that the exact source mapping has been fixed.

### All parent contribution routes

graph: supported. Targets: ENVO:00000562.

The confirmed City location-as-genus claim is removed through the exact source-path/expected-parent guard. ENVO:00000002 remains the sole independent genus. The full-corpus regression proves no collateral record or claim changes; the source-to-generic-park equivalence question is separate and remains open.

### Frozen counts, source versions and MIxS roles

quantity: supported. Targets: ENVO:00000562.

gold_ecosystem_paths data row1249: nodes4397&#124;4398, all KGX counters zero. gold_path_biosamples row664 has8 BIOSAMPLEs; gold_studies row1092 links Gs0118444. PREGO habitat row354 has8 TAXONs,8 direct assertions,score3,annotated_genomes_isolates. Taxa rows5104-5111 reproduce all8, direct TRUE, no corroboration. Decisions rows1383 and1447 ITEM REVIEW GOLD.fc89e5f170/PREGO.527b7f4fea; PATHS row596; ontology named parent row5240. The organic-layer triad row1070 uses park as local scale for another path, not target identity evidence. Current member counts are not substituted for frozen counts or summed across units. No contextual triad is adopted as target identity.

### Native status, history and reproduction

provenance: supported. Targets: ENVO:00000562.

Both prior ITEM decisions and native EXACT/REVIEWED state are preserved, not re-endorsed or promoted. Native exclusion history is appended. Verified review lineage resolves only F1; F2/F3 remain open under their stable keys.

### Optional parameters, literature, graphs and datasets

completeness: supported. Targets: ENVO:00000562.

The whole target and contributing inventories were inspected. Empty optional slots are not negative biological evidence. No parameter, causal edge, definition or characteristic-organism claim is inferred from external study examples or unrelated parent/child records. The only newly authored target input is the guarded parent exclusion; it does not supply missing ecological evidence.

### Structured expression-module applicability

evidence: not_applicable. Targets: ENVO:00000562.

No gene, regulator, protein or transcriptomic claim triggers iModulonDB. Not invoking that adapter is not evidence against habitat eligibility.

### Native checks and scientific limits

schema: supported. Targets: ENVO:00000562.

Post-correction focused checks, corpus reproduction, history, semantic bundle and generated site verification passed. Final product-commit full QC is separately recorded in C3/E7; mechanical checks do not resolve the remaining scientific scope questions.

### Every emitted taxon and source confidence semantics

evidence: concern. Targets: ENVO:00000562.

All seven supplied labels agree with current NCBI names. Of the eight requested IDs,1830138 resolves to90970 Alicyclobacillus tolerans and the single-ID response explicitly lists1830138 in AkaTaxIds; the old unlabeled ID is not an unresolvable reference. Dyadobacter1121482 and Thermosphaera633148 are strain rank; the other current records are species rank. All8 frozen associations have score3/direct TRUE and tie-break ranks1-8; these are not abundance, occupancy or characteristic status. PREGO's original per-association evidence was unavailable; one exact strain's primary isolation context was independently inspected.

## Findings

### F1: City location-context parent removed by guarded exclusion

major / resolved / confirmed; issue key: envo-00000562-city-context-parent.

The original confirmed defect has been corrected: ENVO:00000856 is no longer a parent of ENVO:00000562. Exact GOLD path and expected-parent guards suppress only this contribution, while the independent ENVO genus and every other field remain unchanged.

Disposition: Resolved by the maintained exclusion, native regeneration and full-document/corpus regression. The correction does not resolve source equivalence, taxonomy normalization or native REVIEWED status interpretation.

### F2: Urban source qualification is not established as exact generic-park equivalence

major / open / provisional; issue key: gold-fc89e5f170-urban-versus-generic-park-equivalence.

GOLD's City &gt; Park concept maps exactly to ENVO00000562, which PREGO uses generically. All eight recovered GOLD members are city-park surface samples; ENVO's definition is not urban-only, and at least one listed PREGO strain has a national-park hot-spring origin. These observations require reassessing source-level equivalence, but they do not alone define every potential GOLD member or justify a forced split. Removing the City parent does not repair this separate mapping question.

### F3: An unlabeled frozen taxon identifier now has an explicit canonical redirect

minor / open / confirmed; issue key: envo-00000562-merged-taxon-1830138.

The third PREGO entry retains NCBITaxon1830138 without a label. Current NCBI explicitly redirects it to NCBITaxon90970 Alicyclobacillus tolerans. This is a nonblocking normalization/provenance gap, not a broken reference or evidence that the association is biologically false. A naive ID substitution could silently alter deduplication and candidate-pool semantics.

## Recommended Actions And Acceptance Checks

### ACT2

Reassess GOLD.fc89e5f170 at ITEM depth against the full City-qualified source and generic ENVO scope. Decide whether a broader-target relation or separate qualified mint is warranted; preserve PREGO's source identity and taxon provenance. Do not merge or split based solely on sampled membership.

- Write evidence explaining why source and target extensions are equivalent or why a directional/non-identity relation is required.
- Prove PREGO associations are not silently reassigned to an urban-only habitat, and preserve the source-qualified GOLD path.
- Run focused schema/strict validation, corpus reproduction, native history and full QC; run label validation for grounding changes.

### ACT3

Define a governed taxonomy-refresh/alias treatment that preserves the historical PREGO ID and score while exposing the verified canonical identity and label. Do not hand-edit the generated taxon row or recompute historical ranks from a live API without provenance.

- Add a merged-ID regression and verify any deduplication/pool-count effects explicitly.
- Preserve all eight historical association records or document a justified governed transformation with source hashes.
- Run focused schema/strict validation, corpus reproduction, native history and full QC; run label validation for grounding changes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/park.yaml; Entire generated file; immediate parents read as context | supports | Full corrected park record read: ENGINEERED/EXACT/REVIEWED, unchanged ENVO definition, sole parent ENVO:00000002, both GOLD/PREGO source attestations, all eight PREGO taxa and four history events. Only the previous City parent is removed and a SOURCE_PARENT_EXCLUDED event appended. |
| E2 | data/raw/gold_ecosystem_paths.tsv; Exact source keys; all row numbers are 1-based data rows excluding comments/header | supports | gold_ecosystem_paths data row1249: nodes4397&#124;4398, all KGX counters zero. gold_path_biosamples row664 has8 BIOSAMPLEs; gold_studies row1092 links Gs0118444. PREGO habitat row354 has8 TAXONs,8 direct assertions,score3,annotated_genomes_isolates. Taxa rows5104-5111 reproduce all8, direct TRUE, no corroboration. Decisions rows1383 and1447 ITEM REVIEW GOLD.fc89e5f170/PREGO.527b7f4fea; PATHS row596; ontology named parent row5240. The organic-layer triad row1070 uses park as local scale for another path, not target identity evidence. Follow-up: maintained gold_parent_exclusions.tsv data row1 now guards GOLD.fc89e5f170 with exact City &gt; Park path and expected parent ENVO:00000856. |
| E3 | src/habitatmech/seed.py; resolve_gold, apply_decision, ingest_gold, ontology and GOLD parent contribution, build_document | supports | The exact source-parent guard now suppresses only ENVO:00000856 from GOLD.fc89e5f170. Independent ontology ENVO:00000002 remains. Full-corpus before/after comparison proves only ENVO:00000562 changes, only parent_habitats and one appended audit event differ. Both ITEM source decisions, exact mapping, all source counters/units and all eight taxa remain identical; no status promotion or taxonomy refresh. |
| E4 | https://gold.jgi.doe.gov/download?mode=site_excel; Complete Biosample, Organism, SequencingProject and Study sheets | partial | Eight exact-path BioSamples Gb0135247-Gb0135254, workbook rows11268-11275, describe metal, mixed metal/plastic and wood surfaces in New York City parks. Project rows82611-82618 link Gp0134876-Gp0134883, PRJNA271013 and Gs0118444; Study row23944 describes urban/subway/public-surface sampling. Classification row181 retains node4398. No exact-path Organism rows. These are sample/material observations, not whole-park replicates or eight PREGO taxa. Complete census: 244951/532019/636914/63806 rows including headers. This Oct9 snapshot is later than frozen provenance. |
| E5 | https://gold.jgi.doe.gov/download?mode=ecosystempaths; site data, 2422 rows after reset_dimensions; terminal row stated in E4 | context_only | The exact terminal classification persists; prefix descendants were separately distinguished and never counted as exact target members. |
| E6 | curation/; history/; research/; reports/; reviews/; data/raw/; Historical baseline search plus explicit source-hash comparison and new correction artifacts | context_only | The baseline ignored-inclusive search is retained as historical scope evidence, not repeated absence certification. The newly saved 20261009T201157Z-park bundle, exact maintained exclusion and native park history now exist. Prior source/term-request/overlay search limitations remain. All64 captured post-correction input hashes match both current bytes and the retained correction revision; only the park record and exclusion table differ from the original61. |
| E8 | CLAUDE.md; Semantic invariants; docs/CURATION.md; HabitatRecord, SourceAttestation, GroundingStatusEnum and CharacteristicTaxon schema | supports | Parents must be strictly broader. Source mapping endpoints are source concept -&gt; record ID. Counts require their units; PREGO score/rank is not abundance or characteristic status. REVIEWED requires ITEM decisions for all merged sources. A review bundle does not itself promote status. |
| S1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:00000562; Active terms and their official parent endpoints: ENVO:00000562, ENVO:00000002, ENVO:00000856 | supports | Official ENVO park denotes bounded land/water set aside for recreation/conservation and has independent anthropogenic-geographic-feature parent ENVO:00000002. City ENVO:00000856 denotes an incorporated populated place. These inspected definitions support excluding a city-location context from strict park ancestry; they do not settle urban GOLD versus generic PREGO equivalence. |
| S2 | https://doi.org/10.4056/sigs.821804; PMID21304709 / PMC3035292 fullTextXML, Abstract and Introduction; DSM11486=M11TL | supports | The genome paper places Thermosphaera aggregans DSM11486 in water/sediment from Obsidian Pool, Yellowstone National Park. It supports a specific national-park-associated hot-spring context, not generic urban park ecology or the provenance of all PREGO rows. |
| S3 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1830138; TaxId90970, ScientificName Alicyclobacillus tolerans, AkaTaxIds/TaxId1830138 | supports | A single-ID lookup confirms an explicit taxonomic redirect, with source update date2025-09-05. The old CURIE resolves but lacks a current display label/normalization trail in the emitted record. |
| S4 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1121482,1124743,1830138,29344,33950,341202,622637,633148; Bulk XML:33 requested IDs across two records,33 returned Taxon entries,zero XML errors | supports | All seven supplied labels agree with current NCBI names. Of the eight requested IDs,1830138 resolves to90970 Alicyclobacillus tolerans and the single-ID response explicitly lists1830138 in AkaTaxIds; the old unlabeled ID is not an unresolvable reference. Dyadobacter1121482 and Thermosphaera633148 are strain rank; the other current records are species rank. All8 frozen associations have score3/direct TRUE and tie-break ranks1-8; these are not abundance, occupancy or characteristic status. PREGO's original per-association evidence was unavailable; one exact strain's primary isolation context was independently inspected. |
| S5 | https://doi.org/10.3390/microorganisms10020293; PMID35208748 / PMC8879827 fullTextXML, methods2.1/2.3 and AppendixC | supports | PREGO combines heterogeneous evidence channels with channel-specific confidence formulas bounded(0,5]. Fixed resource confidence for genome/isolate evidence differs from environmental-sample co-occurrence. These scores are not abundance, prevalence, occupancy or a claim of characteristic biology. |
| E9 | reviews/structured/20261009T201157Z-park/review.yaml; F1,F2,F3,entire original observation | supports | Immutable original review establishes the confirmed City-parent defect, provisional urban/generic equivalence concern and minor taxonomy-alias gap. This follow-up preserves each issue_key and exact previous_occurrences; it does not silently close unresolved findings. |
| E10 | tests/test_park_parent.py; test_park_exclusion_preserves_sources_taxa_and_other_records | supports | Fresh focused regression passed. It removes only the new exclusion in memory, rebuilds both whole corpora, proves equal membership with exactly one changed document and semantic row, retains every other field and previous event, and explicitly checks frozen source nodes, exact mapping, 8 TAXON/score3, ranks/pool and unchanged 1830138 gap. |
| E11 | history/mappings/park/2026-10-09T201914Z-codex-gpt-5-3b9f60.yaml; Entire scaffolded and validated curation session | supports | Native append-only history attributes the guarded exclusion to codex-gpt-5/gpt-5/codex, links #1818 and explicitly leaves #1819/#1820 open. It records tested scope without rewriting original source decisions. |
| E12 | https://github.com/CultureBotAI/HabitatMech/actions/runs/37986401900; Locked Linux rebuild at bf924eac64712ae5e57de81b7209284ab0470dc9 and downloaded artifact | supports | One changed Park vector encoded; repeat reused1; full embed reused3208. Real32-point canary and full PaCMAP projections executed. Downloaded/local full input bytes identical (SHA256197442d85ec7f200a9429609c7a871011c36a74e03338f968ac0ea206d580346). Native checker validates current bundle and cache;3208 unique finite points and unchanged membership. Only Park semantic row changes, although reprojection changes coordinates globally. |
| E7 | https://github.com/CultureBotAI/HabitatMech/actions/runs/37986995717; Successful product commit0ca31955971a7ccd42b8e4bcaf37f72b6a0e979c; raw log saved build/review-20261009o-product-qc.log | supports | Successful authoritative product-commit QC:650 passed,3 skipped;225 native history records,3208 closed-schema records and exact corpus reproduction,32 overlays,curation floor,site,redirects,term requests and all quality gates passed. Raw CI log inspected; no final-head result is preclaimed. Fresh local focused schema,strict,history,corpus,reproduction,labels,review/publication and render checks also passed. Optional local-runtime and premature-download limitations are explicit in C14/C15 and resolved operationally through successful Linux/C10 verification. |

## Limits And Additional Notes

- Original GOLD node/edge and frozen August membership were not recovered in bounded searches. The later public workbook is not a replacement for frozen provenance.
- All source and ontology searches are bounded. Missing examples or optional values do not establish biological absence or justify invented identities.
- QC skips3 tests; label validation skips2057 no-adapter terms. These deterministic checks do not establish scientific correctness.
- All emitted taxonomy labels/IDs were checked, but original PREGO per-association evidence was unavailable. Confidence scores do not prove characteristic biology; not every association was independently verified against primary ecological evidence.
- Locked numerical inference is unavailable on this Mac architecture; successful unchanged Linux runtime and local artifact verification supply the map-build evidence. The premature incomplete-download check was rerun successfully after terminal download completion.
- Same-agent follow-up, not independent scientific approval. Entire corrected record read; unchanged primary-source observations retain their original actual access timestamps.
- Only F1 is resolved. F2/#1819 and F3/#1820 remain open. No optional biological assertions, identity decision or taxonomy normalization were added.
- All64 captured scientific inputs match retained correction commit bf924eac64712ae5e57de81b7209284ab0470dc9 and current scientific bytes. Its annotated record-review-base tag is published and verified to peel exactly to that revision.
- Original observation is immutable and retains the pre-correction parent. New generated map/site products were separately checked against these corrected inputs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T204039Z-park-followup
kind: record
repository: CultureBotAI/HabitatMech
title: 'park: verified correction at bf924eac6 and retained scope findings'
started_at: '2026-10-09T20:21:32Z'
finished_at: '2026-10-09T20:40:39Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent continuing scientific review and separately authorized
    publication; no independent scientific approval claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The guarded City-context parent exclusion is verified and resolves F1/#1818.
  The generic ENVO genus, both source attestations and all eight historical PREGO
  taxa are unchanged. Urban/generic source equivalence and merged-taxonomy normalization
  remain open; this is not an independent scientific approval or a clean scientific
  pass.
source:
  git_revision: bf924eac64712ae5e57de81b7209284ab0470dc9
  state: git_commit
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 4544b5d2c11fbbb3a46cd8a65f7e664363df78c1000c590aab533219f9eec59b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: d429c8bb74f521df9a77a90b216a44fc6959ee28efb1fa17a93582536caa8bce
    role: context
  - path: CLAUDE.md
    sha256: 98d95f910ff5160bc5b2ff572766785519dacdba487700bebaa6dbf96d071fd9
    role: context
  - path: conf/id_label_targets.yaml
    sha256: e100d84aabccaeb00c1a60246142b3cafcec009dbfba58f5cc319c35adddb633
    role: context
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: 0602cca13e6495da256a6f1cfd5897462f73f9739a729447862017d93c148efd
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: cc4da2e7e5e8750e6c023683014aa37a909230280f231eec5be7c71795340312
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: e9c815eec1b8721ce8b07274ec5645910ed90bd378a1af887096b7ad4f60791c
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/samples/class_swept_unscreened-20260814.tsv
    sha256: 27fce2849781b21f8fdb434aaaffac0f55e51bef84f1c1ea7d7feecd11d8471e
    role: context
  - path: curation/term_requests.tsv
    sha256: 9977e384b79128d6e89c85f28e35c77d29644d503dea6d53c12628599e33f7f3
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/engineered/bioreactor.yaml
    sha256: c0a5f4d06130d949810c29b15f5874b4e9673b23dc188161d699412c2bea0c02
    role: context
  - path: data/habitats/engineered/chemical_product.yaml
    sha256: d5039d8e0f3f8c77680371d162d7934f5ada70d63130e5a1b4bcab154bb77b1f
    role: context
  - path: data/habitats/engineered/city.yaml
    sha256: 3a52eece16e4be7b9a7d1d19a57cfaac92dcb6e97c7a0bd3ef08dddad0814c7a
    role: context
  - path: data/habitats/engineered/industrial_wastewater.yaml
    sha256: 07698df721a169cd55c2d1ce80027df8c8a3140536ba99eee312272887ce8768
    role: context
  - path: data/habitats/engineered/material.yaml
    sha256: 01b2767b0983a3ed85de20b759119f14102b6c1333dad051466e7b94667ffa02
    role: context
  - path: data/habitats/engineered/organic_dairy_farm.yaml
    sha256: c8c647d25e2d4731f1ee7bd714952d1ca00a15ccca48b0710a2f26ce955feb0c
    role: context
  - path: data/habitats/engineered/organic_waste_material.yaml
    sha256: 8f0f59b82c69cc6ba5fab56d4bf40c3cf33ac8eb9ab58dd32a4b8b93875cc9c6
    role: context
  - path: data/habitats/engineered/paper.yaml
    sha256: 183ff1a853f7783cb29f0404c05ac67ca018cd93a8ad34cf9e1c101223bc8793
    role: context
  - path: data/habitats/engineered/park.yaml
    sha256: 277c4f3ee5e0fc6a9a077f06ef360f19dea781a6e5a56d52db64c02b7e0d6c65
    role: target
  - path: data/habitats/engineered/partial_nitrification_anammox_pna.yaml
    sha256: bca83d5e1f1c72ea951ec088eaf23ada93822960252f70c081b2a14b8515c957
    role: context
  - path: data/habitats/engineered/pcr_blank_control.yaml
    sha256: 46f5385ddb5c38656a87918cb6a5076d1a9e1abb32a9fb739e8b71988ca3578b
    role: context
  - path: data/habitats/engineered/sheet_of_paper.yaml
    sha256: 6499a0ee1a610df73a6a8b8eb32193ea88e2b45b40850c6b5cbdc627054fad6b
    role: context
  - path: data/habitats/engineered/solid_waste.yaml
    sha256: 4cd78657634aca99d98863d643419c7deb56b8835d9f47d144d08247457736d4
    role: context
  - path: data/raw/GOLD_MANIFEST.yaml
    sha256: 99ec487ae02d512cfb75440685f927abe907effe52cb755feb095631e8841489
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 4657672d429be35e551ceef4a1204ab0a8120558ce63e2a2b74188eee94b8480
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/bacdive_source_taxa.tsv
    sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
    role: context
  - path: data/raw/environment_parameters.tsv
    sha256: a75d0f565d8ee2498188ff98b17d0ab325ae4f782601bf4414eff6e86c13e0f9
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/gold_path_biosamples.tsv
    sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
    role: context
  - path: data/raw/gold_path_triads.tsv
    sha256: b1717bd8fc4fdcd6a1a132f4eb32df3638b01ddf7d78f9a5797f110ee2b1e8d6
    role: context
  - path: data/raw/gold_studies.tsv
    sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
    role: context
  - path: data/raw/isolation_source_groundings.tsv
    sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
    role: context
  - path: data/raw/madin_habitat_taxa.tsv
    sha256: d30854cfcffca0405914d04071ac47053938d354d5df250125843131b7c91fd7
    role: context
  - path: data/raw/madin_habitats.tsv
    sha256: 2ae1756f40242600365c49bfbdada4bce5fc8b86630426bb34892f055e5a5c93
    role: context
  - path: data/raw/ontology_subclass_edges.tsv
    sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
    role: context
  - path: data/raw/ontology_terms.tsv
    sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
    role: context
  - path: data/raw/prego_habitat_taxa.tsv
    sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
    role: context
  - path: data/raw/prego_habitats.tsv
    sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
    role: context
  - path: docs/CURATION.md
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: f7aa39ee762d94f1902d9f08f328cb897bc543e4e226057eb4770d24bfcc6eb5
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/mappings/anaerobic_zone/2026-10-07T033547Z-codex-gpt-5-d36e47.yaml
    sha256: f7027c603782fbc30e9e55bdf57d8649607b1ac94275c72fd49df2c8ad17998d
    role: context
  - path: history/mappings/park/2026-10-09T201914Z-codex-gpt-5-3b9f60.yaml
    sha256: fd117c8c88255a42bad7dce3e7648bc85f277e4a96de7b1d66d3f08392899347
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260923T183929Z-aerobic_zone.md
    sha256: 15372ba808c0ef233930195600d9fecff599f58b8379918f765f489554754ed9
    role: context
  - path: reports/yaml_record_review/20260924T104251Z-sheet_of_paper.md
    sha256: cc4f1ac519d0e5d7d73e3f38ef6cc034385b7e565e506f2909d81cf538118edb
    role: context
  - path: reports/yaml_record_review/20261007T032222Z-anaerobic_zone.md
    sha256: 0d18ff1020121cf559347efe6f1fe8a54e6ff0b134a23cafafb60e04ab7b5e3a
    role: context
  - path: reports/yaml_record_review/20261007T082502Z-biochar__4f716948.md
    sha256: 996004cbce7c05357e71efb67b9618b6e113c95808203a7a63ae0fc4027051e5
    role: context
  - path: reviews/structured/20261009T201157Z-park/review.yaml
    sha256: d3611449d526ed4d111b535d3232c6c62040dfcf14dd5888e581fe7e56b77013
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 52d2a22309a1f4a10728a663560bb4d918346c292221fd34139b99b4159d3fe5
    role: context
  - path: src/habitatmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/habitatmech/seed.py
    sha256: 92adf631fa099120a497ff7001473e659347d23ac9b418f04cd341ddad5d2a89
    role: context
  - path: tests/test_park_parent.py
    sha256: 1b83a75addc5ea0687c699e15858079644c7fa9694042b82df930a850870b401
    role: context
scope:
  description: Historical review of the entire corrected park record at retained Git
    revision bf924eac64712ae5e57de81b7209284ab0470dc9, with focused verification of
    the City-parent exclusion and retention of both unresolved predecessor findings.
    This assesses that exact revision, not an unspecified current working tree. All64
    scientific input hashes were separately verified identical in the later product
    commit and current files.
  selection: Follow-up of 20261009T201157Z-park after separately authorized correction
    in PR1815.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00000562
  exclusions:
  - target: All other HabitatMech records
    reason: Parents, children, same-label concepts and source examples inform this
      target only.
targets:
- target_id: ENVO:00000562
  path: data/habitats/engineered/park.yaml
  label: park
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input, source transform or generator owner
checks:
- check_id: C1
  name: Corrected schema
  status: passed
  required: true
  target_ids:
  - ENVO:00000562
  command: env UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/park.yaml
  exit_code: 0
  summary: No issues found.
- check_id: C2
  name: Corrected closed schema
  status: passed
  required: true
  target_ids:
  - ENVO:00000562
  command: env UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/park.yaml
  exit_code: 0
  summary: One file,zero errors.
- check_id: C3
  name: Corrected full native QC
  status: passed
  required: true
  target_ids:
  - ENVO:00000562
  command: uv run python scripts/run_qc.py (GitHub Actions run37986995717, product
    commit0ca31955971a7ccd42b8e4bcaf37f72b6a0e979c)
  summary: Successful authoritative product-commit QC:650 passed,3 skipped;225 native
    history records,3208 closed-schema records and exact corpus reproduction,32 overlays,curation
    floor,site,redirects,term requests and all quality gates passed. Raw CI log inspected;
    no final-head result is preclaimed.
  exit_code: 0
- check_id: C4
  name: Fresh ontology labels
  status: passed
  required: true
  target_ids:
  - ENVO:00000562
  command: env UV_CACHE_DIR=build/uv-cache just validate-products > build/review-20261009o-final-labels.log
    2>&1
  exit_code: 0
  summary: 1178 canonical,1 synonym,5 exceptions,2057 no-adapter skips.
- check_id: C5
  name: Trusted-base native review validation
  status: passed
  required: true
  target_ids:
  - ENVO:00000562
  command: env UV_CACHE_DIR=build/uv-cache RECORD_REVIEW_BASE=24829e1d73449a2bd2815b1140099926f8b16ea0
    just review-check
  exit_code: 0
  summary: 55 bundles valid and4 contract tests passed before saving this follow-up.
- check_id: C6
  name: Whole-corpus correction regression
  status: passed
  required: true
  target_ids:
  - ENVO:00000562
  command: env UV_CACHE_DIR=build/uv-cache uv run pytest -q tests/test_park_parent.py
  exit_code: 0
  summary: 1 passed; only park document and semantic input change; every unrelated
    claim and record preserved.
- check_id: C7
  name: Target causal and expression-module checks
  status: not_applicable
  required: false
  target_ids:
  - ENVO:00000562
  summary: No target overlay or gene/expression claim. Baseline full QC validates
    repository-wide causal/reference constraints.
- check_id: C8
  name: Original upstream membership and PREGO association evidence
  status: unavailable
  required: false
  target_ids:
  - ENVO:00000562
  summary: Baseline bounded source-access limitations remain; no new ecological inference
    is substituted for unavailable source evidence.
- check_id: C9
  name: Exact corrected corpus reproduction
  status: passed
  required: true
  target_ids:
  - ENVO:00000562
  command: env UV_CACHE_DIR=build/uv-cache just verify-corpus
  exit_code: 0
  summary: 3208 expected/found,zero missing/extra/differing.
- check_id: C10
  name: Downloaded map and vector verification
  status: passed
  required: true
  target_ids:
  - ENVO:00000562
  command: env UV_CACHE_DIR=build/uv-cache uv run python scripts/embedding_pipeline.py
    check --output build/pr1815-map-download/data/text_map --input build/text-map/inputs-review-o.jsonl
    --cache build/pr1815-map-download/build/text-map/vectors.sqlite
  exit_code: 0
  summary: Passed after artifact download completed. Input bytes match local export;3208
    unique finite points,unchanged membership,only Park semantic row changed.
- check_id: C11
  name: Generated site verification
  status: passed
  required: true
  target_ids:
  - ENVO:00000562
  command: env UV_CACHE_DIR=build/uv-cache just render-check
  exit_code: 0
  summary: 3208 habitat pages,252 redirects,8 categories,114 term requests; pages
    in step with corpus.
- check_id: C12
  name: Native session history
  status: passed
  required: true
  target_ids:
  - ENVO:00000562
  command: env UV_CACHE_DIR=build/uv-cache just validate-history history/mappings/park/2026-10-09T201914Z-codex-gpt-5-3b9f60.yaml
  exit_code: 0
  summary: One native history record valid.
- check_id: C13
  name: Review-base publication durability
  status: passed
  required: true
  target_ids:
  - ENVO:00000562
  command: env UV_CACHE_DIR=build/uv-cache uv run pytest -q tests/test_record_review_publication.py
  exit_code: 0
  summary: 2 tests passed; separately verified published annotated tag peels exactly
    to bf924eac64712ae5e57de81b7209284ab0470dc9.
- check_id: C14
  name: Local locked numerical runtime
  status: failed
  required: false
  target_ids:
  - ENVO:00000562
  command: env HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 UV_CACHE_DIR=build/uv-cache
    uv run --locked --project conf/embedding-runtime python -c 'import torch, pacmap;
    print(torch.__version__)'
  exit_code: 2
  summary: Locked Torch2.14.0 has no macOS x86_64 wheel. Used unchanged locked Linux
    runtime in successful run37986401900; no dependency workaround or pin change.
- check_id: C15
  name: Initial artifact check before download completion
  status: failed
  required: false
  target_ids:
  - ENVO:00000562
  command: env UV_CACHE_DIR=build/uv-cache uv run python scripts/embedding_pipeline.py
    check --output build/pr1815-map-download/data/text_map --input build/text-map/inputs-review-o.jsonl
    --cache build/pr1815-map-download/build/text-map/vectors.sqlite
  exit_code: 1
  summary: Premature check found no current.json while artifact download was still
    running. Same download was awaited to terminal success; subsequent complete-artifact
    check C10 passed. Not a validation failure of the finished bundle.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/park.yaml
  locator: Entire generated file; immediate parents read as context
  accessed_at: '2026-10-09T20:38:01Z'
  support: supports
  summary: 'Full corrected park record read: ENGINEERED/EXACT/REVIEWED, unchanged
    ENVO definition, sole parent ENVO:00000002, both GOLD/PREGO source attestations,
    all eight PREGO taxa and four history events. Only the previous City parent is
    removed and a SOURCE_PARENT_EXCLUDED event appended.'
- evidence_id: E2
  kind: record_content
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Exact source keys; all row numbers are 1-based data rows excluding comments/header
  accessed_at: '2026-10-09T20:38:01Z'
  support: supports
  summary: 'gold_ecosystem_paths data row1249: nodes4397|4398, all KGX counters zero.
    gold_path_biosamples row664 has8 BIOSAMPLEs; gold_studies row1092 links Gs0118444.
    PREGO habitat row354 has8 TAXONs,8 direct assertions,score3,annotated_genomes_isolates.
    Taxa rows5104-5111 reproduce all8, direct TRUE, no corroboration. Decisions rows1383
    and1447 ITEM REVIEW GOLD.fc89e5f170/PREGO.527b7f4fea; PATHS row596; ontology named
    parent row5240. The organic-layer triad row1070 uses park as local scale for another
    path, not target identity evidence. Follow-up: maintained gold_parent_exclusions.tsv
    data row1 now guards GOLD.fc89e5f170 with exact City > Park path and expected
    parent ENVO:00000856.'
- evidence_id: E3
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: resolve_gold, apply_decision, ingest_gold, ontology and GOLD parent contribution,
    build_document
  accessed_at: '2026-10-09T20:38:01Z'
  support: supports
  summary: The exact source-parent guard now suppresses only ENVO:00000856 from GOLD.fc89e5f170.
    Independent ontology ENVO:00000002 remains. Full-corpus before/after comparison
    proves only ENVO:00000562 changes, only parent_habitats and one appended audit
    event differ. Both ITEM source decisions, exact mapping, all source counters/units
    and all eight taxa remain identical; no status promotion or taxonomy refresh.
- evidence_id: E4
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Complete Biosample, Organism, SequencingProject and Study sheets
  accessed_at: '2026-10-09T20:11:57Z'
  support: partial
  summary: 'Eight exact-path BioSamples Gb0135247-Gb0135254, workbook rows11268-11275,
    describe metal, mixed metal/plastic and wood surfaces in New York City parks.
    Project rows82611-82618 link Gp0134876-Gp0134883, PRJNA271013 and Gs0118444; Study
    row23944 describes urban/subway/public-surface sampling. Classification row181
    retains node4398. No exact-path Organism rows. These are sample/material observations,
    not whole-park replicates or eight PREGO taxa. Complete census: 244951/532019/636914/63806
    rows including headers. This Oct9 snapshot is later than frozen provenance.'
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: E5
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  locator: site data, 2422 rows after reset_dimensions; terminal row stated in E4
  accessed_at: '2026-10-09T20:11:57Z'
  support: context_only
  summary: The exact terminal classification persists; prefix descendants were separately
    distinguished and never counted as exact target members.
  snapshot_sha256: 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396
- evidence_id: E6
  kind: search
  reference: curation/; history/; research/; reports/; reviews/; data/raw/
  locator: Historical baseline search plus explicit source-hash comparison and new
    correction artifacts
  accessed_at: '2026-10-09T20:38:01Z'
  support: context_only
  summary: The baseline ignored-inclusive search is retained as historical scope evidence,
    not repeated absence certification. The newly saved 20261009T201157Z-park bundle,
    exact maintained exclusion and native park history now exist. Prior source/term-request/overlay
    search limitations remain. All64 captured post-correction input hashes match both
    current bytes and the retained correction revision; only the park record and exclusion
    table differ from the original61.
  search_scope: 'No gitignore filtering: Path.rglob and rg --no-ignore --hidden. Expected
    GOLD_nodes.tsv, GOLD_edges.tsv and goldData.xlsx also searched under build, data/raw
    and configured kg-microbe/data. Configured transformed/prego is missing. These
    are bounded local-source misses, not global absence claims.'
- evidence_id: E8
  kind: record_content
  reference: CLAUDE.md
  locator: Semantic invariants; docs/CURATION.md; HabitatRecord, SourceAttestation,
    GroundingStatusEnum and CharacteristicTaxon schema
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: Parents must be strictly broader. Source mapping endpoints are source concept
    -> record ID. Counts require their units; PREGO score/rank is not abundance or
    characteristic status. REVIEWED requires ITEM decisions for all merged sources.
    A review bundle does not itself promote status.
- evidence_id: S1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:00000562
  locator: 'Active terms and their official parent endpoints: ENVO:00000562, ENVO:00000002,
    ENVO:00000856'
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: Official ENVO park denotes bounded land/water set aside for recreation/conservation
    and has independent anthropogenic-geographic-feature parent ENVO:00000002. City
    ENVO:00000856 denotes an incorporated populated place. These inspected definitions
    support excluding a city-location context from strict park ancestry; they do not
    settle urban GOLD versus generic PREGO equivalence.
- evidence_id: S2
  kind: primary_source
  reference: https://doi.org/10.4056/sigs.821804
  locator: PMID21304709 / PMC3035292 fullTextXML, Abstract and Introduction; DSM11486=M11TL
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: The genome paper places Thermosphaera aggregans DSM11486 in water/sediment
    from Obsidian Pool, Yellowstone National Park. It supports a specific national-park-associated
    hot-spring context, not generic urban park ecology or the provenance of all PREGO
    rows.
- evidence_id: S3
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1830138
  locator: TaxId90970, ScientificName Alicyclobacillus tolerans, AkaTaxIds/TaxId1830138
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: A single-ID lookup confirms an explicit taxonomic redirect, with source
    update date2025-09-05. The old CURIE resolves but lacks a current display label/normalization
    trail in the emitted record.
- evidence_id: S4
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1121482,1124743,1830138,29344,33950,341202,622637,633148
  locator: Bulk XML:33 requested IDs across two records,33 returned Taxon entries,zero
    XML errors
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: All seven supplied labels agree with current NCBI names. Of the eight requested
    IDs,1830138 resolves to90970 Alicyclobacillus tolerans and the single-ID response
    explicitly lists1830138 in AkaTaxIds; the old unlabeled ID is not an unresolvable
    reference. Dyadobacter1121482 and Thermosphaera633148 are strain rank; the other
    current records are species rank. All8 frozen associations have score3/direct
    TRUE and tie-break ranks1-8; these are not abundance, occupancy or characteristic
    status. PREGO's original per-association evidence was unavailable; one exact strain's
    primary isolation context was independently inspected.
- evidence_id: S5
  kind: primary_source
  reference: https://doi.org/10.3390/microorganisms10020293
  locator: PMID35208748 / PMC8879827 fullTextXML, methods2.1/2.3 and AppendixC
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: PREGO combines heterogeneous evidence channels with channel-specific confidence
    formulas bounded(0,5]. Fixed resource confidence for genome/isolate evidence differs
    from environmental-sample co-occurrence. These scores are not abundance, prevalence,
    occupancy or a claim of characteristic biology.
- evidence_id: E9
  kind: prior_review
  reference: reviews/structured/20261009T201157Z-park/review.yaml
  locator: F1,F2,F3,entire original observation
  accessed_at: '2026-10-09T20:38:01Z'
  support: supports
  summary: Immutable original review establishes the confirmed City-parent defect,
    provisional urban/generic equivalence concern and minor taxonomy-alias gap. This
    follow-up preserves each issue_key and exact previous_occurrences; it does not
    silently close unresolved findings.
- evidence_id: E10
  kind: validation
  reference: tests/test_park_parent.py
  locator: test_park_exclusion_preserves_sources_taxa_and_other_records
  accessed_at: '2026-10-09T20:38:01Z'
  support: supports
  summary: Fresh focused regression passed. It removes only the new exclusion in memory,
    rebuilds both whole corpora, proves equal membership with exactly one changed
    document and semantic row, retains every other field and previous event, and explicitly
    checks frozen source nodes, exact mapping, 8 TAXON/score3, ranks/pool and unchanged
    1830138 gap.
- evidence_id: E11
  kind: record_content
  reference: history/mappings/park/2026-10-09T201914Z-codex-gpt-5-3b9f60.yaml
  locator: Entire scaffolded and validated curation session
  accessed_at: '2026-10-09T20:38:01Z'
  support: supports
  summary: 'Native append-only history attributes the guarded exclusion to codex-gpt-5/gpt-5/codex,
    links #1818 and explicitly leaves #1819/#1820 open. It records tested scope without
    rewriting original source decisions.'
- evidence_id: E12
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/37986401900
  locator: Locked Linux rebuild at bf924eac64712ae5e57de81b7209284ab0470dc9 and downloaded
    artifact
  accessed_at: '2026-10-09T20:38:01Z'
  support: supports
  summary: One changed Park vector encoded; repeat reused1; full embed reused3208.
    Real32-point canary and full PaCMAP projections executed. Downloaded/local full
    input bytes identical (SHA256197442d85ec7f200a9429609c7a871011c36a74e03338f968ac0ea206d580346).
    Native checker validates current bundle and cache;3208 unique finite points and
    unchanged membership. Only Park semantic row changes, although reprojection changes
    coordinates globally.
- evidence_id: E7
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/37986995717
  locator: Successful product commit0ca31955971a7ccd42b8e4bcaf37f72b6a0e979c; raw
    log saved build/review-20261009o-product-qc.log
  accessed_at: '2026-10-09T20:38:01Z'
  support: supports
  summary: Successful authoritative product-commit QC:650 passed,3 skipped;225 native
    history records,3208 closed-schema records and exact corpus reproduction,32 overlays,curation
    floor,site,redirects,term requests and all quality gates passed. Raw CI log inspected;
    no final-head result is preclaimed. Fresh local focused schema,strict,history,corpus,reproduction,labels,review/publication
    and render checks also passed. Optional local-runtime and premature-download limitations
    are explicit in C14/C15 and resolved operationally through successful Linux/C10
    verification.
assessments:
- assessment_id: A1
  area: identity
  topic: Physical habitat and source identity
  outcome: supported
  summary: The generic ENVO park definition covers recreation/conservation areas,
    not only urban parks and not incorporated settlements. Current GOLD examples substantiate
    city-park surfaces. A primary genome paper for PREGO-listed Thermosphaera aggregans
    DSM11486 instead gives a Yellowstone hot-spring water/sediment origin. This supports
    keeping generic-park geography distinct from urban source qualification; it does
    not prove how PREGO generated every association.
  target_ids:
  - ENVO:00000562
  evidence_ids:
  - E1
  - E2
  - E4
  - S1
  - S2
- assessment_id: A2
  area: grounding
  topic: Exact identity, source mapping and broader scope
  outcome: concern
  summary: PREGO self-identity is explicit. The GOLD EXACT mapping is based on the
    bare leaf and an ITEM REVIEW note; the City qualification and recovered urban
    samples make generic equivalence questionable. A supported broad mapping or retained
    qualified mint may be appropriate, but sample examples alone do not establish
    the source vocabulary's entire intended extension. The separately corrected City
    parent is not evidence that the exact source mapping has been fixed.
  target_ids:
  - ENVO:00000562
  evidence_ids:
  - E1
  - E2
  - E3
  - E8
  - S1
- assessment_id: A3
  area: graph
  topic: All parent contribution routes
  outcome: supported
  summary: The confirmed City location-as-genus claim is removed through the exact
    source-path/expected-parent guard. ENVO:00000002 remains the sole independent
    genus. The full-corpus regression proves no collateral record or claim changes;
    the source-to-generic-park equivalence question is separate and remains open.
  target_ids:
  - ENVO:00000562
  evidence_ids:
  - E1
  - E3
  - E8
  - S1
  - E9
  - E10
  - E11
- assessment_id: A4
  area: quantity
  topic: Frozen counts, source versions and MIxS roles
  outcome: supported
  summary: 'gold_ecosystem_paths data row1249: nodes4397|4398, all KGX counters zero.
    gold_path_biosamples row664 has8 BIOSAMPLEs; gold_studies row1092 links Gs0118444.
    PREGO habitat row354 has8 TAXONs,8 direct assertions,score3,annotated_genomes_isolates.
    Taxa rows5104-5111 reproduce all8, direct TRUE, no corroboration. Decisions rows1383
    and1447 ITEM REVIEW GOLD.fc89e5f170/PREGO.527b7f4fea; PATHS row596; ontology named
    parent row5240. The organic-layer triad row1070 uses park as local scale for another
    path, not target identity evidence. Current member counts are not substituted
    for frozen counts or summed across units. No contextual triad is adopted as target
    identity.'
  target_ids:
  - ENVO:00000562
  evidence_ids:
  - E1
  - E2
  - E4
  - E5
  - E8
- assessment_id: A5
  area: provenance
  topic: Native status, history and reproduction
  outcome: supported
  summary: Both prior ITEM decisions and native EXACT/REVIEWED state are preserved,
    not re-endorsed or promoted. Native exclusion history is appended. Verified review
    lineage resolves only F1; F2/F3 remain open under their stable keys.
  target_ids:
  - ENVO:00000562
  evidence_ids:
  - E1
  - E2
  - E3
  - E9
  - E10
  - E11
- assessment_id: A6
  area: completeness
  topic: Optional parameters, literature, graphs and datasets
  outcome: supported
  summary: The whole target and contributing inventories were inspected. Empty optional
    slots are not negative biological evidence. No parameter, causal edge, definition
    or characteristic-organism claim is inferred from external study examples or unrelated
    parent/child records. The only newly authored target input is the guarded parent
    exclusion; it does not supply missing ecological evidence.
  target_ids:
  - ENVO:00000562
  evidence_ids:
  - E1
  - E2
  - E6
  - E8
- assessment_id: A7
  area: evidence
  topic: Structured expression-module applicability
  outcome: not_applicable
  summary: No gene, regulator, protein or transcriptomic claim triggers iModulonDB.
    Not invoking that adapter is not evidence against habitat eligibility.
  target_ids:
  - ENVO:00000562
  evidence_ids:
  - E1
- assessment_id: A8
  area: schema
  topic: Native checks and scientific limits
  outcome: supported
  summary: Post-correction focused checks, corpus reproduction, history, semantic
    bundle and generated site verification passed. Final product-commit full QC is
    separately recorded in C3/E7; mechanical checks do not resolve the remaining scientific
    scope questions.
  target_ids:
  - ENVO:00000562
  evidence_ids:
  - E7
- assessment_id: A9
  area: evidence
  topic: Every emitted taxon and source confidence semantics
  outcome: concern
  summary: All seven supplied labels agree with current NCBI names. Of the eight requested
    IDs,1830138 resolves to90970 Alicyclobacillus tolerans and the single-ID response
    explicitly lists1830138 in AkaTaxIds; the old unlabeled ID is not an unresolvable
    reference. Dyadobacter1121482 and Thermosphaera633148 are strain rank; the other
    current records are species rank. All8 frozen associations have score3/direct
    TRUE and tie-break ranks1-8; these are not abundance, occupancy or characteristic
    status. PREGO's original per-association evidence was unavailable; one exact strain's
    primary isolation context was independently inspected.
  target_ids:
  - ENVO:00000562
  evidence_ids:
  - E1
  - E2
  - E3
  - S4
  - S5
findings:
- finding_id: F1
  issue_key: envo-00000562-city-context-parent
  category: graph
  severity: major
  status: resolved
  certainty: confirmed
  title: City location-context parent removed by guarded exclusion
  description: 'The original confirmed defect has been corrected: ENVO:00000856 is
    no longer a parent of ENVO:00000562. Exact GOLD path and expected-parent guards
    suppress only this contribution, while the independent ENVO genus and every other
    field remain unchanged.'
  target_ids:
  - ENVO:00000562
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - E2
  - E3
  - E4
  - S1
  - E9
  - E10
  - E11
  - E12
  rule_id: HabitatMech native identity, strictly-broader parent, evidence-scope and
    provenance rules
  native_severity: major
  normalization_reason: Material identity, hierarchy or source-representation concern.
    Provisional findings retain uncertainty and do not authorize guessed corrections.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator for proposed correction
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261009T201157Z-park
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1818
  disposition_reason: Resolved by the maintained exclusion, native regeneration and
    full-document/corpus regression. The correction does not resolve source equivalence,
    taxonomy normalization or native REVIEWED status interpretation.
- finding_id: F2
  issue_key: gold-fc89e5f170-urban-versus-generic-park-equivalence
  category: grounding
  severity: major
  status: open
  certainty: provisional
  title: Urban source qualification is not established as exact generic-park equivalence
  description: GOLD's City > Park concept maps exactly to ENVO00000562, which PREGO
    uses generically. All eight recovered GOLD members are city-park surface samples;
    ENVO's definition is not urban-only, and at least one listed PREGO strain has
    a national-park hot-spring origin. These observations require reassessing source-level
    equivalence, but they do not alone define every potential GOLD member or justify
    a forced split. Removing the City parent does not repair this separate mapping
    question.
  target_ids:
  - ENVO:00000562
  field_paths:
  - source_attestations[0].mapping_predicate
  - grounding_status
  evidence_ids:
  - E1
  - E2
  - E3
  - E4
  - S1
  - S2
  - E9
  - E10
  rule_id: HabitatMech native identity, strictly-broader parent, evidence-scope and
    provenance rules
  native_severity: major
  normalization_reason: Material identity, hierarchy or source-representation concern.
    Provisional findings retain uncertainty and do not authorize guessed corrections.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator for proposed correction
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261009T201157Z-park
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1819
- finding_id: F3
  issue_key: envo-00000562-merged-taxon-1830138
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: An unlabeled frozen taxon identifier now has an explicit canonical redirect
  description: The third PREGO entry retains NCBITaxon1830138 without a label. Current
    NCBI explicitly redirects it to NCBITaxon90970 Alicyclobacillus tolerans. This
    is a nonblocking normalization/provenance gap, not a broken reference or evidence
    that the association is biologically false. A naive ID substitution could silently
    alter deduplication and candidate-pool semantics.
  target_ids:
  - ENVO:00000562
  field_paths:
  - characteristic_taxa[2].taxon_id
  - characteristic_taxa[2].taxon_label
  evidence_ids:
  - E1
  - E2
  - S3
  - S4
  - E9
  - E10
  rule_id: HabitatMech native identity, strictly-broader parent, evidence-scope and
    provenance rules
  native_severity: minor
  normalization_reason: Nonblocking label/normalization provenance gap; source identifier
    remains resolvable.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator for proposed correction
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained input or generator for proposed correction
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261009T201157Z-park
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1820
actions:
- action_id: ACT2
  description: Reassess GOLD.fc89e5f170 at ITEM depth against the full City-qualified
    source and generic ENVO scope. Decide whether a broader-target relation or separate
    qualified mint is warranted; preserve PREGO's source identity and taxon provenance.
    Do not merge or split based solely on sampled membership.
  finding_ids:
  - F2
  target_ids:
  - ENVO:00000562
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator for proposed correction
  acceptance_checks:
  - Write evidence explaining why source and target extensions are equivalent or why
    a directional/non-identity relation is required.
  - Prove PREGO associations are not silently reassigned to an urban-only habitat,
    and preserve the source-qualified GOLD path.
  - Run focused schema/strict validation, corpus reproduction, native history and
    full QC; run label validation for grounding changes.
  generator: Native maintained-input curation -> just seed -> just seed-canary ENVO:00000562
    -> just seed-apply --force -> just render; no hand-edited generated records.
- action_id: ACT3
  description: Define a governed taxonomy-refresh/alias treatment that preserves the
    historical PREGO ID and score while exposing the verified canonical identity and
    label. Do not hand-edit the generated taxon row or recompute historical ranks
    from a live API without provenance.
  finding_ids:
  - F3
  target_ids:
  - ENVO:00000562
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator for proposed correction
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained input or generator for proposed correction
  acceptance_checks:
  - Add a merged-ID regression and verify any deduplication/pool-count effects explicitly.
  - Preserve all eight historical association records or document a justified governed
    transformation with source hashes.
  - Run focused schema/strict validation, corpus reproduction, native history and
    full QC; run label validation for grounding changes.
  generator: Native maintained-input curation -> just seed -> just seed-canary ENVO:00000562
    -> just seed-apply --force -> just render; no hand-edited generated records.
limitations:
- Original GOLD node/edge and frozen August membership were not recovered in bounded
  searches. The later public workbook is not a replacement for frozen provenance.
- All source and ontology searches are bounded. Missing examples or optional values
  do not establish biological absence or justify invented identities.
- QC skips3 tests; label validation skips2057 no-adapter terms. These deterministic
  checks do not establish scientific correctness.
- All emitted taxonomy labels/IDs were checked, but original PREGO per-association
  evidence was unavailable. Confidence scores do not prove characteristic biology;
  not every association was independently verified against primary ecological evidence.
- Locked numerical inference is unavailable on this Mac architecture; successful unchanged
  Linux runtime and local artifact verification supply the map-build evidence. The
  premature incomplete-download check was rerun successfully after terminal download
  completion.
notes:
- Same-agent follow-up, not independent scientific approval. Entire corrected record
  read; unchanged primary-source observations retain their original actual access
  timestamps.
- Only F1 is resolved. F2/#1819 and F3/#1820 remain open. No optional biological assertions,
  identity decision or taxonomy normalization were added.
- All64 captured scientific inputs match retained correction commit bf924eac64712ae5e57de81b7209284ab0470dc9
  and current scientific bytes. Its annotated record-review-base tag is published
  and verified to peel exactly to that revision.
- Original observation is immutable and retains the pre-correction parent. New generated
  map/site products were separately checked against these corrected inputs.
tags:
- habitat
- engineered
- gold
- record-review
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261009T201157Z-park
  relationship: Verified correction of F1; explicit open successors for F2 and F3.
```
