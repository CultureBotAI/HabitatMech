# How the source vocabularies are harmonized

This is the design record for `src/habitatmech/seed.py`. It exists so that
the decisions below are arguable rather than merely implemented — if one looks
wrong, the place to push back is here.

Numerical measurements in this design record describe the August 2026 source
snapshots identified by `data/raw/MANIFEST.yaml` and
`data/raw/GOLD_MANIFEST.yaml`; they are historical evidence, not live corpus
statistics. Run `just report` for current corpus counts.

## The pipeline

```
kg-microbe checkout
   │  habitatmech.extract                    (needs kg-microbe; run rarely)
   ▼
data/raw/*.tsv  +  provenance manifests     (committed and reviewable)
   │  habitatmech.seed                       (needs nothing else)
   ▼
data/habitats/<category>/<slug>.yaml        (generated HabitatRecords)
```

The split matters: the multi-gigabyte KGX dumps are not vendored, but everything
downstream of the inventories runs — and is testable — without kg-microbe
present. `data/raw/MANIFEST.yaml` records the kg-microbe inputs;
`data/raw/GOLD_MANIFEST.yaml` records the later GOLD bulk-export and API inputs.
Together they identify source and output bytes so provenance is checkable after
the fact, while the large source dumps remain untracked.

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
identifier become one record with all their attestations. Run `just report` for
the current record and multi-source counts.

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

### The composed route is exempt from the rule

The composed-label routes deliberately do **not** apply the shallowest-claims
guard, and that asymmetry is intentional rather than an oversight. The composed
label already carries the path context, so the matched term is not broader than
the path the way `sediment` is broader than `marine sediment`: `UBERON:0001977`
*is* blood serum whether the host is a human or a bird, and the host
distinction belongs to the taxon, not to the habitat term. Applying the guard
would mint three near-identical serum records, which is worse than one.

Six terms are consequently claimed by more than one GOLD path and merged:

| Term | Paths merged |
|---|---|
| `UBERON:0001977` blood serum | Mammals: Human / Mammals / Birds `> Circulatory system > Blood > Serum` |
| `ENVO:00002129` anaerobic sludge | Bioreactor `> Anaerobic`, `> DHS reactor > Anaerobic`, `> MBR > Anaerobic` |
| `UBERON:0001913` milk | Mammals: Human / Mammals `> Mammary gland > Milk` |
| `ENVO:00000546` lake sediment | Freshwater `> Lake`, Non-marine Saline and Alkaline `> Lake` |
| `UBERON:0001969` blood plasma | Mammals: Human / Mammals |
| `UBERON:0000965` eye lens | Mammals: Human / Mammals |

Every path survives in `source_attestations` with its full `source_path`, so no
provenance is lost. But `anaerobic sludge` across three bioreactor types is a
weaker case than the anatomical ones, and nothing currently distinguishes
"the prefix context is immaterial" (serum) from "the prefix context is material"
(reactor type). Tracked in issue #15.

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

## Filenames are pinned, not recomputed

`data/habitats/PATHS.tsv` maps each identifier to its slug, and is committed.
It exists because recomputing filenames is not stable.

Two habitats can share a label — "Sediment" appears under several GOLD paths
and, once minted separately, several records slug to it. The original scheme
gave the bare slug to whichever same-slug concept sorted first by identifier,
so an upstream refresh that added a lower-sorting concept silently renamed the
incumbent: a delete + add in the diff for a record whose content identity never
changed. Many files require collision-resolved slugs, so this is not a corner
case; `data/habitats/PATHS.tsv` is the live inventory.

With the lockfile:

- a concept already listed keeps its slug, always — nothing about the rest of
  the corpus can move it;
- a new concept takes `slugify(label)`, or `<base>__<id hash>` if that is
  taken. If both are taken the seeder raises rather than silently colliding;
- slugs are unique **corpus-wide, not per-directory**. The directory comes from
  `habitat_category`, which is heuristic and expected to improve, so records
  will move between categories; corpus-wide uniqueness means a move can never
  collide at its destination;
- the lockfile is rebuilt from the current concept set on every run, so an
  entry whose concept vanished upstream is dropped. It cannot accumulate rot.

Renaming a record is therefore a deliberate edit to `PATHS.tsv` followed by a
re-seed — an explicit, reviewable one-line diff instead of an invisible
consequence of sort order. Because the file is hand-editable and its slugs
become filenames, `load_lockfile()` rejects anything outside `[a-z0-9_]`; a
slug containing a path separator would write outside the corpus.

A record that changes category leaves its old file behind. `habitatmech.seed`
reports such stale files on every run and deletes them with `--prune`, which is
ignored on `--only` / `--limit` runs because a partial run's path set is not
authoritative — it would otherwise propose deleting the entire corpus.

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


## Class-level sweep

Most of `curation/decisions.tsv` is not individual research, and the file says
so explicitly rather than letting the volume imply otherwise.

Each decision carries a `review_depth`. `ITEM` means the concept was examined
against its source path and its candidate terms. `CLASS` means it was decided
as a member of a mechanically-defined group, and exactly one group exists: the
concept's label matched **no** term in the vendored ENVO/UBERON/FOODON/BTO slice
by any of

* exact label,
* plural/singular of the label,
* slash, parenthetical, or colon variants (undoing GOLD's formatting
  conventions — `Phylloplane/Leaf`, `AGS (Aerobic granular sludge)`,
  `Abscess: Furuncle/Boil`),
* the label composed with its parent path level, in both orders,
* whole-word substring against every term label.

That claim is reproducible: re-run `just worklist` and `scripts/propose_decisions.py`.

**What the sweep does not establish is whether the concept is a habitat at
all.** An earlier version of the note asserted that these were "real habitats
with no term that fits, and therefore ENVO term-request candidates"; they are
not known to be either. Pulling the obvious non-habitats back out — diseases,
interventions, sampling artefacts, `Unclassified` fillers — moved 48 concepts to
individually-decided `NOT_APPLICABLE`, and there are certainly more among the
remainder.

Consequently **`CLASS` decisions do not promote a record to `REVIEWED`**, and a
grounding may never be `CLASS` depth: asserting that a concept *is* a particular
ontology term is always a per-item judgement. `just report` shows the three
buckets — individually-examined term requests, class-swept, and wholly undecided
— separately, so the sweep can never be mistaken for curation.


## Taxon ranking, and what the evidence says about it

Issue #8 observed that PREGO's scores for a large habitat all sit at the top of
the range — 8,715 taxa for soil between 4.0000 and 4.0073 — and proposed ranking
by evidence-channel breadth or direct-assertion count instead. Both proposals
are testable, so `scripts/audit_taxon_ranking.py` tested them, and both turn out
to be **worse**:

| signal, across soil's 8,715 taxa | distinct values |
|---|---:|
| max PREGO score | **2,869** |
| distinct evidence items | 4 |
| direct assertions | 4 |
| distinct channels | 2 |

A signal taking four values cannot order 8,715 taxa. The score is the finest
one available, and switching to any of the alternatives would replace a weak
ordering with an almost totally flat one.

Whether the score's ordering *means* anything is a separate question, and BacDive
answers it. It reaches taxa by a completely different route — isolation source →
strain → taxon, counted by strains actually isolated — so for the habitats both
sources attest, the overlap between PREGO's top-25 and BacDive's taxa is a check
no reasoning about the scores can substitute for. Against the baseline of what
that overlap would be if PREGO's order were random:

```
top-25 hits: 25    expected by chance: 11.0    enrichment: 2.27x
```

So the ranking is **not arbitrary**, which is what the issue assumed. It is
still weak, and the sample is six habitats, so this is evidence against
replacing it rather than evidence that it is good.

Three things follow, and all three are in the data rather than only here:

* the ranking is kept, because the measurement says the alternatives are worse;
* every taxon carries `rank` **and** `candidate_pool`, so "rank 1 of 8,715"
  cannot be misread as "rank 1 of 12" — the record states its own weakness;
* taxa asserted by *both* sources carry `corroborated_by` and are listed first.
  56 entries qualify. Agreement between text-mining and strain-counting is not
  one method agreeing with itself, which makes those the only entries in the
  field with genuinely independent support, and the best `is_characteristic`
  candidates for a curator.

Re-run `python3 scripts/audit_taxon_ranking.py` after any upstream refresh; if
the enrichment drops toward 1.0, the ranking has stopped carrying signal and
should be revisited.
