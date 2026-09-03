# HabitatRecord review checklist

Use this checklist for one generated habitat record and all source concepts
feeding it. It does not require every optional slot to be populated.

## Evidence standard

- Trace every claim to a decision row, term request, or source inventory before
  treating it as curated.
- Verify ontology IDs and canonical labels against the vendored slice/source.
- Source occurrence and association do not establish habitat identity,
  characteristic taxa, or mechanism by themselves.
- Put claim-level evidence on causal edges and other curator-authored claims.
- Preserve conflicts and describe negative searches as bounded “not found.”

## Field-by-field audit

| Area | Verify | Complete enough when |
|---|---|---|
| Identity | Minted/source ID, label, category, source path, and habitat meaning agree. | Disease, process, material, sample artifact, quality, and host-taxon boundaries are explicit. |
| Grounding | Decision enum, target ID/label, relation direction, status, and review depth agree. | Exact identity is ITEM-reviewed; broader terms remain parents, not identities. |
| Definition | Authored text/source, genus parent, and `ADD`/`REPLACE` mode are supported. | Source-derived true parents are not removed merely for preference. |
| Hierarchy | Ontology, source-path, ambiguous-leaf, and term-request parents are all strictly broader. | Related terms are xrefs and no cycle or false is-a remains. |
| Attestations | Source ID/label/path, predicate, count/unit, score, channels, and notes agree. | Unlike units are not compared or summed as one measure. |
| Parameters | Parameter/value, unit/qualifier, MIxS triad role, and source context agree. | A contextual triad term is not automatically promoted to identity. |
| Taxa | Taxon ID/label, assertion source, rank/score, corroboration, and characteristic wording agree. | Reported-from is not upgraded to characteristic without evidence. |
| Evidence/graphs | Reference, snippet/locator, node/edge direction, scope, and claim support agree. | Every causal edge has real evidence independent of habitat attestation. |
| Discussions/datasets | Each item is relevant, durable, and actionable. | Missing maintained input paths are reported rather than bypassed. |
| Status/audit | All source decisions, generated mapping status, and generated history agree. | REVIEWED means every contributing concept has ITEM review. |
