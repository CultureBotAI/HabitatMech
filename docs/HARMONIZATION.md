# How the three source vocabularies are harmonized

This is the design record for `scripts/seed_from_sources.py`. It exists so that
the decisions below are arguable rather than merely implemented — if one looks
wrong, the place to push back is here.

## The pipeline

```
kg-microbe checkout
   │  scripts/extract_source_inventory.py   (needs kg-microbe; run rarely)
   ▼
data/raw/*.tsv  +  MANIFEST.yaml            (committed, reviewable, ~3 MB)
   │  scripts/seed_from_sources.py          (needs nothing else)
   ▼
data/habitats/<category>/<slug>.yaml        (3,299 HabitatRecords)
```

The split matters: the multi-gigabyte KGX dumps are not vendored, but everything
downstream of the inventories runs — and is testable — without kg-microbe
present. `data/raw/MANIFEST.yaml` records the byte size, mtime, and sha256 of
every input the inventories were built from, so their provenance is checkable
after the fact.

## Why the inventories are shaped the way they are

**GOLD.** The upstream tree has 4,226 ecosystem nodes but only 1,609 distinct
labels, because a node exists per (path, source-record) pairing and unfilled
levels repeat the literal `Unclassified`. Collapsing on the filler-stripped
path yields 2,562 distinct ecosystem concepts, with the per-node assertion
counts summed across the nodes that collapse together. Three nodes
("Sediment", "Mid stream", "Low land river systems") are detached roots
upstream with no parent and no assertions; they survive as thin records.

Labels come from `data/raw/gold/GOLD_nodes.tsv`, not the transformed copy — the
transformed nodes carry the label "Unclassified" for *every* ecosystem node.

**PREGO.** PREGO asserts up to ~8,700 taxa for a single habitat, so the full
habitat-taxon matrix is neither committable nor useful inline. The extractor
keeps the top 25 per habitat by score and records the untruncated total as
`taxon_count`, so the truncation is visible rather than silent.

**Ontology slice.** ENVO and BTO are vendored whole (~3.9k and ~6.6k terms);
UBERON and FOODON are vendored only where a label or synonym matches a source
label, since they are 25k and 39k terms of mostly-irrelevant anatomy and food
products. All ancestors are pulled in transitively so the hierarchy is
self-contained — `tests/test_inventories.py` fails on any subclass edge that
leaves the slice, because a dangling parent would silently truncate the
ancestor walk that categorisation depends on.

An earlier cut kept referenced-terms-only and grounded barely a third of GOLD:
the terms GOLD's labels would have matched were never in the pool to match
against. Grounding quality is bounded by the label pool.

## Identity and merging

Merge key is the resolved identifier. Source concepts resolving to the same
identifier become one record with all their attestations; 3,443 source concepts
become 3,299 records, 128 of them multi-source.

Concepts with no defensible ontology term get a **content-hashed minted
identifier** — `habitatmech:GOLD.<10 hex of sha1(canonical_path)>`. Hashing
rather than sequential numbering means adding a concept never renumbers its
neighbours, so a re-seed after an upstream refresh diffs only where the data
actually changed.

## The anti-conflation rule

The one decision most likely to be "simplified" by a later contributor, and the
one that would do the most damage.

Ten GOLD paths end in the leaf "Soil". Ninety-seven end in "Sediment". Grounding
every one of them to the matching ontology term would merge marine, freshwater,
and hot-spring sediment into a single `ENVO:00002007` record whose attestations
and assertion counts mix habitats that are not the same habitat.

So: for a given leaf label, **only the shallowest path may claim the term**.
Depth in GOLD's tree is specificity — the depth-3
`Environmental > Terrestrial > Soil` is what ENVO means by soil, and everything
below it is a *kind* of soil. Deeper paths get a minted identifier, grounding
status `NARROW`, and the matched term as a `parent_habitats` entry, which is
what the relationship actually is.

When several paths tie at the shallowest depth, **nobody claims the term**.
`...Mammals: Human > ... > Fecal` and `...Birds > ... > Fecal` are both depth 5
and neither is what an ontology means by feces, so both become NARROW children.
This costs coverage (296 ambiguous leaves are tied versus 97 with a unique
shallowest path) and is the right trade: an unclaimed term is a curation task,
a wrongly claimed one is silent data corruption.

The composed two-level label is tried *first* for exactly this reason —
"marine sediment" is a real ENVO term and a strictly better grounding than
"sediment", so when it hits, the ambiguity never arises.

## Deferring to upstream curation

kg-microbe's `isolation_source_to_ontology.tsv` has a row for all 162 BacDive
sources. 71 have an empty target with a note explaining why — "abortion-as-event
has no clean isolation-source ontology". Those stay `UNGROUNDED`. Re-grounding
them here by lexical match would overwrite a human decision with a guess, and
the guess would look identical to a real mapping in the output.

13 point at ontologies that describe habitats rather than being them — PATO
qualities, CHEBI chemicals, NCBITaxon organisms. Those become
`NOT_APPLICABLE` with the target kept as an xref: the information survives, but
the record does not claim to *be* a quality.

## Two status fields, deliberately

`grounding_status` is how well the identifier fits the source concept.
`mapping_status` is whether a human has reviewed the record. They are
independent, and collapsing them would force a curator to either lie about a
grounding or refuse to sign off on a record that is genuinely correct except
that no ontology term exists for it. A record can be `REVIEWED` and
`UNGROUNDED`; that combination is a well-formed ENVO term request.

## What the seeder does not do

- It does not set `mapping_status: REVIEWED`. Ever. Lexical matching produces
  plausible groundings, not verified ones.
- It does not write `causal_graphs`. Mechanism claims need citations, and there
  is no upstream source to take them from.
- It does not set `is_characteristic` on a taxon. PREGO attests that a taxon was
  *reported from* a habitat, which is weaker than typifying it — and for soil,
  all 8,715 taxa score within 0.007 of each other, so the ranking barely
  discriminates.
