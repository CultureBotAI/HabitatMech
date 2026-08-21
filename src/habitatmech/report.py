#!/usr/bin/env python3
"""Corpus report over data/habitats/.

Answers the questions a curator actually has about the seeded corpus: how much
of it is grounded, which records are corroborated by more than one source, and
where the ungrounded mass sits (those are the ENVO term-request backlog).

Usage:
    python3 scripts/habitat_report.py
    python3 scripts/habitat_report.py --out reports/corpus.tsv
    python3 scripts/habitat_report.py --ungrounded-top 40
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from habitatmech.seed import HABITAT_PREFIXES as _IDENTITY_PREFIXES
from habitatmech.seed import mint, norm_label

REPO_ROOT = Path(__file__).resolve().parents[2]
HABITATS_DIR = REPO_ROOT / "data" / "habitats"

# The prefixes a habitat record's identifier may use. Imported rather than
# copied: the flag it drives separates "a wrong id here becomes a record" from
# "a wrong id here is only an xref", and a second copy would quietly stop
# flagging any prefix the seeder later gains (#48).

# How an upstream mapping's object label relates to the words in the subject it
# claims to map. The seeder's label check (#39, #41) compares the object_id
# against the object_label and catches a mismatch between the two; it is blind
# by construction when they agree and the *mapping* is still wrong. These
# cohorts are the screen for that second defect class. Measured over the 280
# grounded rows: 136 identical, 62 overlap, 42 subset, 40 disjoint.
COHORTS = {
    # The object label is exactly the subject. Nothing a curator adds here that
    # the mechanical check does not already cover.
    "identical": "no review needed",
    # Shares words, neither contains the other — "acid mine drainage" ->
    # "acid mine drainage site". Low risk.
    "overlap": "low risk",
    # The object's words are a strict subset of the subject's: the mapping
    # dropped modifiers. "Cooling-tower" -> Tower, "Sterilized-plant-part" ->
    # Part. Half of these are fine, because the subject is an enumeration
    # ("Feces-Stool" -> feces) — so this ranks, it does not decide.
    "subset": "modifiers dropped; over-generic targets and merges live here",
    # No shared word: matched on a synonym or a scientific name. Mostly right
    # ("Chicken" -> Gallus gallus), but over-NARROWING hides here — "Reptilia"
    # -> Lepidosauria drops turtles and crocodilians.
    "disjoint": "synonym match; over-narrowing hides here",
}
RISK_COHORTS = ("subset", "disjoint")


# Tops of the "this term is an ORGANISM" hierarchies, reachable now that #46
# vendors ancestry for referenced terms. This is the one defect an exact label
# match cannot catch and #69 could not screen for: NCIT:C77916 "Protozoa" IS
# labelled Protozoa, and is a taxon rather than a place.
#
# UBERON:0000468 was added after this screen reported 0 while being blind to
# the case that actually occurred (#109). It is precise here — it reaches 6
# identities and 6 parent terms, all of them organisms or life stages, and
# nothing else. FOODON's own "organism material" root is NOT usable for this:
# it also reaches cheese, ice cream, milk, leaf, bone marrow and wood, which
# are legitimate habitats.
ORGANISM_ROOTS = {
    "NCIT:C14250", "mesh:D056890", "mesh:D056891",
    "UBERON:0000468",  # multicellular organism
}

# Any term in a taxonomy is an organism, so the prefix settles it without
# needing ancestry. Nothing in the corpus matches today; this is a guard
# against a re-seed introducing one, which is the failure mode that let the
# FOODON case sit unnoticed.
ORGANISM_PREFIXES = ("NCBITaxon:",)

# Roots of "this term is a PROCESS". MIxS rules a process out of the
# environmental triad in the same sentence that rules out organisms and groups
# of organisms, and CLAUDE.md now quotes it — so the corpus should be checked
# for it the same way. Found four records claiming a habitat is-a
# ENVO:06105023 "biofouling", which ENVO defines as "a fouling PROCESS during
# which biological matter accumulates on a solid surface" (#127).
PROCESS_ROOTS = {
    "ENVO:02500000",  # environmental system process
    "GO:0008150",     # biological_process
    "ENVO:03000009",  # material accumulation process
}


def _is_process(term: str, parents: dict[str, list[str]]) -> bool:
    """A term whose ancestry reaches a process root.

    Ancestry only, never the label: FOODON:00002645 "food material by process"
    is a MATERIAL classified by the process that made it, and a label test
    flags it. Fermented and preserved food are habitats.
    """
    return bool(_ancestors(term, parents) & PROCESS_ROOTS)

# FOODON taxa that no organism root reaches, because FOODON files the organism
# under a "<X> material" parent: `algae` -> `algae material` -> `organism
# material`. There is no structural signal separating the taxon from the
# material in that branch, so these are pinned by hand and each is verified
# against its own definition by a test — `algae` is "an informal term for a
# large, diverse group of photosynthetic eukaryotic ORGANISMS", `mollusc` is
# "a large phylum of invertebrate animals", `lichen` is "a composite ORGANISM".
ORGANISM_TERMS = {
    "FOODON:03411301",  # algae
    "FOODON:03411743",  # red algae
    "FOODON:03412395",  # brown algae
    "FOODON:03412502",  # green algae
    "FOODON:03412266",  # seaweed
    "FOODON:03411261",  # fungus
    "FOODON:03412345",  # lichen
    "FOODON:03412112",  # mollusc
    "FOODON:03411433",  # shellfish species
    "FOODON:00002581",  # aquatic invertebrate
    "FOODON:03411021",  # fish or lower water animal
}


def _is_organism(term: str, parents: dict[str, list[str]]) -> bool:
    return (
        term.startswith(ORGANISM_PREFIXES)
        or term in ORGANISM_TERMS
        or bool(_ancestors(term, parents) & ORGANISM_ROOTS)
    )


def _ancestors(term: str, parents: dict[str, list[str]], limit: int = 14) -> set[str]:
    seen: set[str] = set()
    frontier, depth = [term], 0
    while frontier and depth < limit:
        nxt = []
        for node in frontier:
            for parent in parents.get(node, ()):
                if parent not in seen:
                    seen.add(parent)
                    nxt.append(parent)
        frontier, depth = nxt, depth + 1
    return seen


def _organism_identities(records: list[tuple[Path, dict]]) -> list[tuple]:
    """Records that claim an organism is a habitat — as their identity, or as a
    broader habitat.

    Checking only the identity is what let the FOODON algae case through (#109).
    `parent_habitats` means "broader habitats", so an organism there is the same
    over-claim one level up, and it is the level that PROPAGATES: the seeder
    derives a GOLD child's parent from its path node, so one wrong identity on
    `Host-associated > Algae` put "is-a algae, the organism group" into 14
    records. The identity was one defect; the parents were fourteen.

    Two kinds of hit, and they are NOT the same judgement:

    * A **taxonomic grouping** — FOODON's `algae`, "an informal term for a
      large, diverse group of photosynthetic eukaryotic organisms" — can never
      be a habitat. A group of taxa is not a place. These are defects, and a
      test pins them at zero.
    * A **life stage** — UBERON's `larva`, `embryo`, `pupa` — names an organism
      at a stage, and an insect larva plausibly IS a habitat, in the same way
      this corpus treats a sponge or a mammal as one. Whether it should instead
      keep its own identity with a term request, as the host clades do, is a
      curation call and not a thing to sweep along with the first kind.

    A screen that returns nothing because it is broken looks exactly like one
    that returns nothing because the corpus is clean, so a test pins that it
    still detects NCIT:C77916 and still rejects NCIT:C17649 (#46, #69).
    """
    edges_path = REPO_ROOT / "data" / "raw" / "ontology_subclass_edges.tsv"
    if not edges_path.exists():
        return []
    parents: dict[str, list[str]] = defaultdict(list)
    with edges_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            parents[row["subject"]].append(row["object"])
    out = []
    for _, doc in records:
        identifier = doc.get("identifier", "")
        assertions = sum(
            a.get("assertion_count") or 0 for a in doc.get("source_attestations") or []
        )
        # An identity a curator signed off on is their call; a parent is not,
        # because parents are derived by the seeder from the path and from the
        # ontology's own edges. So REVIEWED exempts the identity and never the
        # parents.
        reviewed = doc.get("mapping_status") == "REVIEWED"
        if not identifier.startswith("habitatmech:") and not reviewed:
            if _is_organism(identifier, parents):
                out.append((assertions, identifier, doc.get("label", ""), "identity"))
            elif _is_process(identifier, parents):
                out.append((assertions, identifier, doc.get("label", ""), "process-id"))
        for parent in doc.get("parent_habitats") or []:
            if parent.startswith("habitatmech:"):
                continue
            if _is_organism(parent, parents):
                out.append((assertions, identifier, f"{doc.get('label', '')} -> {parent}",
                            "parent"))
            elif _is_process(parent, parents):
                out.append((assertions, identifier, f"{doc.get('label', '')} -> {parent}",
                            "process"))
    return sorted(out, reverse=True)


def _words(text: str) -> set[str]:
    return {w for w in norm_label(text).split() if w}


# Longest suffix an inflection may add before two labels stop counting as the
# same word: "compost"/"composting" is 3, and nothing useful is longer.
_INFLECTION_SLACK = 3


def label_cohort(subject: str, object_label: str) -> str:
    subject_words, object_words = _words(subject), _words(object_label)
    if not object_words:
        return "overlap"

    # Word-set comparison alone calls "Wastewater" -> "waste water" and
    # "Composting" -> "compost" disjoint, which is a tokenization artefact
    # rather than a mapping defect. Comparing the labels with the spaces taken
    # out catches both, and dropping a short inflectional tail catches the
    # second. Deliberately narrow: it must not swallow "Cooling-tower" ->
    # "Tower", where the missing word is the whole of the meaning.
    flat_subject, flat_object = "".join(sorted(subject_words)), "".join(sorted(object_words))
    joined_subject = norm_label(subject).replace(" ", "")
    joined_object = norm_label(object_label).replace(" ", "")
    if flat_subject == flat_object or joined_subject == joined_object:
        return "identical"
    longer, shorter = sorted((joined_subject, joined_object), key=len, reverse=True)
    if shorter and longer.startswith(shorter) and len(longer) - len(shorter) <= _INFLECTION_SLACK:
        return "identical"

    if subject_words == object_words:
        return "identical"
    if object_words < subject_words:
        return "subset"
    if not subject_words & object_words:
        return "disjoint"
    return "overlap"


# How a record's own label relates to the label of the source concept that
# grounded it. The mapping cohorts above watch kg-microbe's table; these watch
# the seeder's OWN lexical routes, which ground by matching a source label
# against an ontology term's SYNONYMS and had no guard at all — that is how
# "Coral" became barramundi, a fish whose Bengali name is coral, and "Nodule"
# became a lobule of the cerebellum (#62).
GROUNDING_COHORTS = {
    "same": "label matched; nothing to add",
    "dropped": "record label lost words the source had",
    "narrowed": "record label adds words the source never claimed",
    "disjoint": "no shared word — matched on a synonym, across domains",
}
GROUNDING_RISK = ("disjoint", "narrowed")

# Head nouns an ontology adds as a naming convention rather than as a claim:
# "Laboratory" -> "laboratory facility", "Volcanic" -> "volcanic feature",
# "Rumen mucosa" -> "mucosa of rumen". They narrow nothing.
_GENERIC_HEADS = {
    "anatomical", "area", "biome", "body", "device", "ecosystem", "environment",
    "facility", "feature", "gland", "material", "network", "of", "or", "organ",
    "pair",
    "part", "piece", "procedure", "product", "region", "segment", "sheet",
    "structure", "system", "type", "whole", "zone",
}
_CURIE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+$")


def _stems(text: str) -> set[str]:
    """Words with a trailing plural 's' folded off.

    `label_cohort` compares whole joined labels, so it folds "compost"/
    "composting" but not "Plants"/"plant-associated environment" — the
    inflection is on one word inside a longer phrase. Without this, every
    plural source label reads as a cross-domain synonym match and buries the
    real ones.
    """
    return {w[:-1] if len(w) > 3 and w.endswith("s") else w for w in _words(text)}


def grounding_cohort(source_label: str, record_label: str, source_path: str = "") -> str:
    # PREGO nodes carry no label of their own, so the attestation repeats the
    # CURIE. Comparing a CURIE to a label is meaningless and always "disjoint".
    if _CURIE.match(source_label.strip()):
        return "same"
    source_words, record_words = _stems(source_label), _stems(record_label)
    if not source_words or not record_words:
        return "same"
    if label_cohort(source_label, record_label) == "identical":
        return "same"
    if source_words < record_words:
        # The added words are only a claim if the source did not already carry
        # them. GOLD's path usually does: "Sediment" grounded to "marine
        # sediment" looks like an over-claim until you see the path is
        # Environmental > Aquatic > Marine > Sediment. Checking that is what
        # separates a real over-narrowing from the seeder correctly using the
        # context it was given (#67).
        #
        # It compares stems, so a path word and a label word that mean the same
        # thing still read as an addition: GOLD's "... > Heart > Septum" grounded
        # to "cardiac septum" is correct and still flagged. That is the right way
        # round for a screen — it over-reports rather than hiding a real claim.
        claimed = _stems(source_path) | _GENERIC_HEADS
        return "same" if (record_words - source_words) <= claimed else "narrowed"
    if record_words < source_words:
        return "dropped"
    if not source_words & record_words:
        return "disjoint"
    return "same"


def load_records(root: Path) -> list[tuple[Path, dict]]:
    records = []
    for path in sorted(root.rglob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        if isinstance(doc, dict):
            records.append((path, doc))
    return records


def table(title: str, counts: Counter, total: int) -> None:
    print(f"\n=== {title} ===")
    for key, count in counts.most_common():
        share = f"{100 * count / total:5.1f}%" if total else "    -"
        print(f"  {str(key):26s} {count:6d}  {share}")


def _unverifiable_mapping_targets() -> list[tuple[str, str, str, bool]]:
    """Upstream mapping targets whose label the seeder cannot check.

    The check compares an upstream row's `object_label` against the ontology's
    own label, which is what stops a wrong id reaching a record. It can only run
    for terms in the vendored slice, so anything outside it passes unexamined —
    and that silence is worth printing, because upstream has a measured error
    rate on the rows that can be checked (#41).
    """
    raw = REPO_ROOT / "data" / "raw"
    terms_path, mapping_path = raw / "ontology_terms.tsv", raw / "isolation_source_groundings.tsv"
    if not terms_path.exists() or not mapping_path.exists():
        return []
    with terms_path.open(newline="", encoding="utf-8") as fh:
        known = {r["term_id"] for r in csv.DictReader(fh, delimiter="\t")}
    out = []
    with mapping_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            target = (row.get("object_id") or "").strip()
            if target and target not in known:
                out.append((
                    row.get("subject_label", ""), target, row.get("object_label", ""),
                    target.split(":", 1)[0] in _IDENTITY_PREFIXES,
                ))
    return sorted(out, key=lambda r: (not r[3], r[0]))


def _stale_class_sweeps(class_swept: set[str], records: list[tuple[Path, dict]]) -> list[tuple]:
    """Class-swept concepts the growing slice has since given a match.

    A class-level sweep asserts a NEGATIVE — "no term in the vendored slice
    matched this label by exact, variant or composed search". That is a claim
    about the SLICE, not the concept, and it decays as the slice grows.
    Vendoring PO (#10) and the referenced ancestry (#46) falsified it for 20 of
    933 swept concepts while each still read as a considered judgement (#12).

    Re-tested with `propose_decisions.classify` — the same function the sweep
    used, so the claim is checked by the code that made it rather than by a
    reimplementation that could drift from it (#84). A concept the sweep put in
    the "none" tier that no longer lands there is a stale decision.
    """
    if not class_swept:
        return []
    try:
        from habitatmech.proposals import PRIORITY, classify
        from habitatmech.seed import OntologyIndex, read_tsv
    except ImportError:
        return []
    ontology = OntologyIndex(read_tsv("ontology_terms.tsv"), read_tsv("ontology_subclass_edges.tsv"))
    # `classify` supplies the variant logic — plural, slash, parenthetical,
    # colon — which is the part worth reusing. Its index is built here rather
    # than by propose_decisions.build_index, which filters to the five grounding
    # ontologies: that is right when proposing a grounding and exactly wrong
    # here, because the staleness this looks for was CAUSED by vendoring NCIT,
    # mesh and CHEBI. Using the filtered index found 0 of the 20 known cases.
    by_label: dict[str, list[tuple[str, str]]] = defaultdict(list)
    by_synonym: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for term_id, term in ontology.terms.items():
        key = norm_label(term["label"])
        if key:
            by_label[key].append((term_id, term["label"]))
        for synonym in (term.get("synonyms") or "").split("|"):
            skey = norm_label(synonym)
            if skey:
                by_synonym[skey].append((term_id, term["label"]))
    # Same ordering build_index applies, with the non-grounding ontologies
    # falling to the end rather than being dropped: an NCIT or mesh match still
    # counts as staleness, but where an ENVO term also matches, that is the one
    # to name. Without this the check reported BTO:0003809 for "soil" instead of
    # ENVO:00001998 — detection was right and the example was misleading (#86).
    for index in (by_label, by_synonym):
        for key in index:
            index[key].sort(key=lambda t: (PRIORITY.get(t[0].split(":", 1)[0], 9), t[0]))
    out = []
    for _, doc in records:
        if doc.get("identifier") not in class_swept:
            continue
        for attestation in doc.get("source_attestations") or []:
            label = attestation.get("source_label") or ""
            if not label:
                continue
            tier, candidates, _ = classify(label, by_label, by_synonym)
            if tier != "none" and candidates:
                assertions = sum(
                    a.get("assertion_count") or 0 for a in doc.get("source_attestations") or []
                )
                out.append((assertions, label, candidates[0][0], doc["identifier"]))
                break
    return sorted(out, reverse=True)


def _kg_microbe_ontologies() -> Path | None:
    """The kg-microbe transformed-ontology directory, or None.

    None rather than an error: kg-microbe is a multi-gigabyte checkout that only
    re-extraction needs, and `just report` has to keep working without it — CI
    runs entirely off data/raw/. The screen that uses this simply reports
    nothing when it is absent, and says so.
    """
    try:
        from habitatmech.extract import default_kg_microbe_root
    except ImportError:
        return None
    root = default_kg_microbe_root()
    if root is None:
        return None
    return Path(root) / "data" / "transformed" / "ontologies"


# Ontologies whose terms are, by construction, not habitats. A swept concept
# whose label matches one of these is evidence about WHAT KIND of thing the
# concept is — the question a class-level sweep explicitly does not ask.
NON_HABITAT_ONTOLOGIES = {
    "chebi": "a chemical",
    "ncbitaxon": "an organism",
    "pato": "a quality",
    "go": "a process or cellular component",
    "mondo": "a disease",
    "hp": "a phenotype",
}


def _non_habitat_candidates(
    class_swept: set[str], records: list[tuple[Path, dict]], kgm: Path | None = None
) -> list[tuple]:
    """Swept concepts whose label names a chemical, organism, quality or disease.

    A class-level sweep records one negative — "no term in the vendored slice
    matched by any search route" — and its note says outright that whether the
    concept is a habitat AT ALL was not assessed. That leaves the question
    nobody has asked of 863 records, and it is the question that decides whether
    each is a term request or a NOT_APPLICABLE.

    Matching against the ontologies that exist to name non-habitats answers it
    from evidence rather than from reading. It RANKS: the path decides, and the
    path routinely overturns the match. "White" under Muscles is white muscle
    tissue, a habitat, not PATO's *white*; "Rubber" under Marine > Waste is a
    substrate microbes colonise, not merely a chemical. Roughly half of what
    this surfaces is a false positive, which is why it produces a worklist and
    not a decision.

    What it is good at is the systematic case. A whole GOLD branch grounded to
    an organism group — Host-associated > Algae to FOODON's *algae*, which
    FOODON defines as "a large, diverse group of photosynthetic eukaryotic
    organisms" — put that organism in the parent_habitats of 14 records, and
    the existing organism-identity screen could not see it because that screen
    tests ancestry against NCIT and mesh roots while FOODON files the organism
    and the material under one shared root.
    """
    if not class_swept:
        return []
    kgm = kgm or _kg_microbe_ontologies()
    if kgm is None or not kgm.exists():
        return []
    index: dict[str, tuple[str, str, str]] = {}
    for ontology, kind in NON_HABITAT_ONTOLOGIES.items():
        path = kgm / f"{ontology}_nodes.tsv"
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if not row.get("name"):
                    continue
                for name in [row["name"], *(row.get("synonym") or "").split("|")]:
                    key = norm_label(name)
                    if key and key not in index:
                        index[key] = (row["id"], row["name"], kind)

    out = []
    for _, doc in records:
        if doc.get("identifier") not in class_swept:
            continue
        for attestation in doc.get("source_attestations") or []:
            hit = index.get(norm_label(attestation.get("source_label") or ""))
            if not hit:
                continue
            assertions = sum(
                a.get("assertion_count") or 0 for a in doc.get("source_attestations") or []
            )
            out.append((assertions, attestation.get("source_label") or "", hit[2], hit[0],
                        doc["identifier"]))
            break
    return sorted(out, reverse=True)


def _compound_path_candidates(
    class_swept: set[str], records: list[tuple[Path, dict]]
) -> list[tuple]:
    """Swept concepts whose <parent> <leaf> path steps name a term, though the
    leaf alone names nothing.

    Every search route the seeder and the sweeps use takes the leaf label on its
    own. But a GOLD leaf is only the last step of a path, and for a whole class
    of anatomy it is an adjective that means nothing by itself:

        Host-associated > ... > Cartilage > Hyaline   -> hyaline cartilage tissue
        Host-associated > ... > Blood > Venous        -> venous blood
        Host-associated > ... > Canthus > Outer       -> outer canthus

    Searching "Hyaline" finds PATO's *transparent*; searching "hyaline
    cartilage" finds UBERON:0001994. So the sweeps' claim — "no term matched by
    any search route" — is true of the routes and false of the concept.

    Both orderings are tried because GOLD is inconsistent about which step
    carries the modifier. Restricted to the habitat-grounding prefixes: the
    leaf-only version of this screen returned 23 candidates that were entirely
    chemicals, host taxa and qualities, none of them a habitat term the sweep
    had missed.

    Ranks; does not decide. The compound is specific enough that precision is
    high, but "specific enough" is not "verified" — each still needs reading
    against its own path.
    """
    if not class_swept:
        return []
    try:
        from habitatmech.seed import HABITAT_PREFIXES, OntologyIndex, read_tsv
    except ImportError:
        return []
    ontology = OntologyIndex(read_tsv("ontology_terms.tsv"), read_tsv("ontology_subclass_edges.tsv"))
    index: dict[str, tuple[str, str]] = {}
    for term_id, term in ontology.terms.items():
        if term_id.split(":", 1)[0] not in HABITAT_PREFIXES:
            continue
        names = [term["label"], *(term.get("synonyms") or "").split("|")]
        for name in names:
            key = norm_label(name)
            if key and key not in index:
                index[key] = (term_id, term["label"])

    out, seen = [], set()
    for _, doc in records:
        identifier = doc.get("identifier")
        if identifier not in class_swept or identifier in seen:
            continue
        for attestation in doc.get("source_attestations") or []:
            steps = [s.strip() for s in (attestation.get("source_path") or "").split(">") if s.strip()]
            if len(steps) < 2:
                continue
            for compound in (f"{steps[-2]} {steps[-1]}", f"{steps[-1]} {steps[-2]}"):
                hit = index.get(norm_label(compound))
                if not hit:
                    continue
                assertions = sum(
                    a.get("assertion_count") or 0 for a in doc.get("source_attestations") or []
                )
                out.append((assertions, " > ".join(steps[-2:]), hit[0], hit[1], identifier))
                seen.add(identifier)
                break
            if identifier in seen:
                break
    return sorted(out, reverse=True)


# What HabitatMech contributes that a given ontology does not already name.
# The project's aim is to supersede ENVO for microbial habitats, so "how many
# habitat concepts do we hold that ENVO has no term for" is the headline
# number, not a curation backlog.
COVERAGE_KINDS = (
    ("named_by_envo", "ENVO names this concept directly"),
    ("named_by_other_obo", "another vendored OBO ontology names it; ENVO does not"),
    ("refines_envo", "no term, but narrower than an ENVO term it hangs under"),
    ("refines_other", "no term, but narrower than a non-ENVO term"),
    ("unnamed", "no ontology term names it or anything above it"),
)


def _same_as_candidates(records: list[tuple[Path, dict]]) -> list[tuple]:
    """Novel concepts from different sources sharing a normalised label.

    Two source concepts merge only when they resolve to the same ONTOLOGY term.
    For a concept no ontology names there is nothing to merge on, so two sources
    describing one habitat produce two permanent records — GOLD's
    "Mammals: Human" and BacDive's "Human" held 40,432 and 11,697 assertions for
    one habitat until a SAME_AS decision joined them (#116).

    A shared label is evidence, not proof, so this RANKS. "Microbial" from GOLD
    and from BacDive may or may not be the same concept, and that is a reading.
    It is also only a lower bound in the other direction: the human case has
    different labels on the two sides and this screen cannot see it.

    Records already merged drop out, because a merged record has one identifier.
    """
    by_label: dict[str, list[tuple]] = defaultdict(list)
    for _, doc in records:
        identifier = doc.get("identifier", "")
        if not identifier.startswith("habitatmech:"):
            continue
        attestations = doc.get("source_attestations") or []
        sources = {a["source"] for a in attestations}
        volume = sum(a.get("assertion_count") or 0 for a in attestations)
        by_label[norm_label(doc.get("label", ""))].append((identifier, sources, volume))

    out = []
    for label, members in by_label.items():
        if len(members) < 2:
            continue
        # Same source twice is the ambiguous-leaf rule working as designed —
        # several GOLD paths end in "Sediment" and they are genuinely distinct.
        # Only a collision ACROSS sources suggests one concept named twice.
        if len({s for _, sources, _ in members for s in sources}) < 2:
            continue
        out.append((sum(v for _, _, v in members), label,
                    [(i, sorted(s), v) for i, s, v in members]))
    return sorted(out, reverse=True)


def _slice_term_labels() -> dict[str, str]:
    """term id -> label for the vendored slice, empty when it is absent."""
    path = REPO_ROOT / "data" / "raw" / "ontology_terms.tsv"
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        return {r["term_id"]: r["label"] for r in csv.DictReader(fh, delimiter="\t")}


def _triad_inventory_review() -> dict[str, list[dict[str, str]]]:
    """Classify every GOLD triad slot before it can enter curator ranking.

    Rejected source annotations remain visible here rather than disappearing
    behind the groundability filter. Label disagreements are also retained even
    though the slice label is authoritative for any proposed decision.
    """
    triads = REPO_ROOT / "data" / "raw" / "gold_path_triads.tsv"
    review: dict[str, list[dict[str, str]]] = {
        "groundable": [],
        "missing": [],
        "organism": [],
        "label_mismatch": [],
    }
    if not triads.exists():
        return review

    slice_terms = _slice_term_labels()
    parents: dict[str, list[str]] = defaultdict(list)
    edges = REPO_ROOT / "data" / "raw" / "ontology_subclass_edges.tsv"
    if edges.exists():
        with edges.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                parents[row["subject"]].append(row["object"])

    with triads.open(newline="", encoding="utf-8") as fh:
        for source_row in csv.DictReader(fh, delimiter="\t"):
            row = dict(source_row)
            term = row["top_term"]
            if _is_organism(term, parents):
                review["organism"].append(row)
                continue
            if term not in slice_terms:
                review["missing"].append(row)
                continue
            row["slice_label"] = slice_terms[term]
            review["groundable"].append(row)
            if row["top_label"] != row["slice_label"]:
                review["label_mismatch"].append(row)
    return review


def _distinct_triad_label_mismatches(
    rows: list[dict[str, str]],
) -> list[tuple[str, str, str]]:
    """Return each distinct term/GOLD-label/slice-label disagreement once."""
    return sorted(
        {
            (row["top_term"], row["top_label"], row["slice_label"])
            for row in rows
        }
    )


def _triad_evidence(
    records: list[tuple[Path, dict]],
    inventory_review: dict[str, list[dict[str, str]]] | None = None,
) -> list[tuple]:
    """Minted records whose GOLD path carries an ENVO triad, ranked by how much
    INDEPENDENT evidence stands behind it.

    GOLD's submitters annotate biosamples with a MIxS triad — env_broad_scale,
    env_local_scale, env_medium. For a record this corpus minted because no
    label matched, that is evidence of a completely different kind: what the
    people who took the sample said its environment was, rather than what a
    string looked like.

    **Ranked by agreeing STUDIES, not samples, and that is the whole point.**
    Of 140 paths where every sample agrees, 122 are one study repeating itself
    — `Environmental > Air > Indoor Air > Dust` is unanimous across 116 samples
    for `sports facility`, which is a fact about one study of a sports centre
    and not about indoor dust. Ranking by sample count puts exactly that case
    on top. Only 18 unanimous paths have two or more studies behind them.

    Ranks; does not decide. A triad is three terms and none of them is
    automatically the record's identity: env_medium is often the material,
    env_broad_scale a biome, and which — if any — the concept IS remains a
    curation judgement. Nothing here bypasses the label-verification gate.
    """
    if inventory_review is None:
        inventory_review = _triad_inventory_review()
    if not any(inventory_review.values()):
        return []

    # A slot is only evidence if its term could ever become a grounding. Two
    # ways it cannot, both found in the inventory (#130). They overlap: the
    # NCBITaxon row is also absent from the slice, but the compatibility review
    # assigns it to the more informative organism/taxon bucket. That partitions
    # the 41 rejected slots into 40 missing-only plus one taxon-valued slot.
    #
    #   * absent from the vendored slice — including five prefixes this repo
    #     does not vendor at all (OBI, AISM, GSSO, MCO, MICRO) and
    #     ENVO:00002002 "obsolete food product", a deprecated term GOLD still
    #     annotates live biosamples with. The seeder's label check would refuse
    #     any of them, so ranking them wastes a curator's attention.
    #   * an organism — NCBITaxon:662107 "phyllosphere metagenome" appears as an
    #     env_local_scale. Per #114 a taxon is not a place, and a metagenome is
    #     not even an organism.
    #
    # Every one of these is currently filtered out anyway, because thinly
    # evidenced annotations are also the malformed ones. That is luck, and this
    # makes it a property.
    by_path: dict[str, dict[str, dict]] = defaultdict(dict)
    for row in inventory_review["groundable"]:
        by_path[row["canonical_path"]][row["slot"]] = row

    out = []
    for _, doc in records:
        identifier = doc.get("identifier", "")
        if not identifier.startswith("habitatmech:"):
            continue
        for attestation in doc.get("source_attestations") or []:
            path = attestation.get("source_path") or ""
            if attestation.get("source") != "GOLD" or path not in by_path:
                continue
            slots = by_path[path]
            # A slot counts as corroborated only when two independent studies
            # assert the same term for it.
            corroborated = sum(
                1 for s in ("broad", "local", "medium")
                if s in slots and int(slots[s]["studies_agreeing"]) >= 2
                and slots[s]["distinct_terms"] == "1"
            )
            studies = max(int(slots[s]["studies"]) for s in slots)
            out.append((corroborated, studies, doc.get("label", ""), path, identifier, slots))
            break
    return sorted(out, key=lambda r: (-r[0], -r[1]))


def _coverage_over_ontologies(records: list[tuple[Path, dict]]) -> tuple[Counter, Counter]:
    """Split the corpus by whether an ontology already names each concept.

    Two numbers fall out and they answer different questions:

    * **New over ENVO** — every record ENVO does not name, whether or not some
      other ontology does. This is the count that matters for superseding ENVO.
    * **New over everything vendored** — records no vendored ontology names at
      all. This is the count of genuinely novel concepts, the ones whose labels
      and definitions HabitatMech has to supply itself.

    A record that merely *hangs under* an ENVO term is counted as new, not
    covered: the ambiguous-leaf rule mints an identifier precisely because the
    matched term is BROADER than the concept, so ENVO naming the parent is not
    ENVO naming the concept. Counting those as covered would understate the
    contribution by 667 records.
    """
    kinds: Counter = Counter()
    assertions: Counter = Counter()
    for _, doc in records:
        identifier = doc.get("identifier", "")
        volume = sum(a.get("assertion_count") or 0 for a in doc.get("source_attestations") or [])
        if not identifier.startswith("habitatmech:"):
            kind = "named_by_envo" if identifier.startswith("ENVO:") else "named_by_other_obo"
        else:
            ontology_parents = [
                p for p in (doc.get("parent_habitats") or []) if not p.startswith("habitatmech:")
            ]
            if any(p.startswith("ENVO:") for p in ontology_parents):
                kind = "refines_envo"
            elif ontology_parents:
                kind = "refines_other"
            else:
                kind = "unnamed"
        kinds[kind] += 1
        assertions[kind] += volume
    return kinds, assertions


def _mapping_cohorts(decided: set[str]) -> tuple[Counter, int, list[tuple]]:
    """Split the upstream mappings by cohort and rank the undecided risky ones.

    A row is "decided" once every source concept it feeds has a per-item entry
    in curation/decisions.tsv, so this shrinks as the review proceeds — like the
    ungrounded backlog, and unlike a one-off audit.

    Both routes into the mapping table are joined. BacDive resolves a source by
    normalized label falling back to slug; GOLD reaches the same table by its
    leaf label. Joining only the first understated the backlog by 52 concepts
    and blamed the gap on rows this corpus does not carry (#52).
    """
    raw = REPO_ROOT / "data" / "raw"
    mapping_path = raw / "isolation_source_groundings.tsv"
    sources_path = raw / "bacdive_isolation_sources.tsv"
    gold_path = raw / "gold_ecosystem_paths.tsv"
    if not mapping_path.exists() or not sources_path.exists():
        return Counter(), 0, []

    # Invert each source's own join so a mapping row can name the minted
    # identifiers a decision would have to key on. Value is (minted id, volume).
    by_key: dict[str, list[tuple[str, int]]] = defaultdict(list)
    with sources_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            entry = (mint("BACDIVE", row["bacdive_id"]), int(row.get("strain_count") or 0))
            for key in (norm_label(row["label"]), norm_label(row["source_slug"])):
                if key:
                    by_key[key].append(entry)
    if gold_path.exists():
        with gold_path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                key = norm_label(row.get("leaf_label", ""))
                if key:
                    by_key[key].append((
                        mint("GOLD", row["canonical_path"]),
                        int(row.get("total_assertions") or 0),
                    ))

    counts: Counter = Counter()
    risky = 0
    backlog = []
    with mapping_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            target = (row.get("object_id") or "").strip()
            if not target:
                continue
            cohort = label_cohort(row["subject_label_normalized"], row["object_label"])
            counts[cohort] += 1
            if cohort not in RISK_COHORTS:
                continue
            risky += 1
            # A source is indexed under several keys that collide for most of
            # them — dedupe or a row lists once per key that matched.
            seen: set[str] = set()
            for identifier, volume in by_key.get(norm_label(row["subject_label"]), ()):
                if identifier in decided or identifier in seen:
                    continue
                seen.add(identifier)
                backlog.append((
                    # A target the seeder would adopt as the record's identity
                    # is worth more attention than one it can only keep as an
                    # xref, so rank on that before assertion volume.
                    target.split(":", 1)[0] in _IDENTITY_PREFIXES,
                    volume, cohort,
                    row["subject_label"], target, row["object_label"], identifier,
                ))
    return counts, risky, sorted(backlog, reverse=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=HABITATS_DIR)
    parser.add_argument("--out", type=Path, help="Write a per-record TSV here.")
    parser.add_argument(
        "--ungrounded-top",
        type=int,
        default=20,
        help="Show the N ungrounded records with the most upstream assertions "
        "(the highest-yield ENVO term requests).",
    )
    args = parser.parse_args(argv)

    if not args.root.exists():
        raise SystemExit(f"no corpus at {args.root}; run `just seed-apply` first")

    # Decisions taken at CLASS depth are recorded but do not promote a record to
    # REVIEWED; reporting them with the wholly-undecided ones would hide that a
    # sweep happened, and with the term requests would overstate it.
    class_swept_ids: set[str] = set()
    # A CLASS-depth sweep did not read the mapping, so it does not clear a row
    # from the cohort backlog; only per-item judgement does.
    item_decided: set[str] = set()
    decisions_path = REPO_ROOT / "curation" / "decisions.tsv"
    if decisions_path.exists():
        with decisions_path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if (row.get("review_depth") or "ITEM").strip().upper() == "CLASS":
                    class_swept_ids.add(row["identifier"])
                else:
                    item_decided.add(row["identifier"])

    records = load_records(args.root)
    total = len(records)
    if not total:
        raise SystemExit(f"no records under {args.root}")

    print(f"=== HabitatMech corpus: {total} records under {args.root.relative_to(REPO_ROOT)} ===")

    by_category: Counter = Counter()
    by_grounding: Counter = Counter()
    by_status: Counter = Counter()
    by_prefix: Counter = Counter()
    by_source: Counter = Counter()
    corroboration: Counter = Counter()
    field_coverage: Counter = Counter()
    # An ungrounded record that a curator has confirmed is a term request;
    # one nobody has looked at yet is backlog. Reporting them together hides
    # all the progress and all the remaining work at once.
    term_requests: list[tuple[int, str, str]] = []
    class_swept: list[tuple[int, str, str]] = []
    undecided: list[tuple[int, str, str]] = []
    source_totals: dict[str, int] = defaultdict(int)
    rows = []

    for path, doc in records:
        identifier = doc.get("identifier", "")
        by_category[doc.get("habitat_category", "?")] += 1
        by_grounding[doc.get("grounding_status", "?")] += 1
        by_status[doc.get("mapping_status", "?")] += 1
        by_prefix[identifier.split(":", 1)[0]] += 1

        attestations = doc.get("source_attestations") or []
        sources = sorted({a.get("source", "?") for a in attestations})
        for source in sources:
            by_source[source] += 1
        corroboration[len(sources)] += 1

        assertions = 0
        for attestation in attestations:
            count = attestation.get("assertion_count") or 0
            assertions += count
            source_totals[attestation.get("source", "?")] += count

        for field in ("definition", "environmental_parameters", "characteristic_taxa",
                      "parent_habitats", "causal_graphs", "evidence"):
            if doc.get(field):
                field_coverage[field] += 1

        if doc.get("grounding_status") == "UNGROUNDED":
            if doc.get("mapping_status") == "REVIEWED":
                bucket = term_requests
            elif identifier in class_swept_ids:
                bucket = class_swept
            else:
                bucket = undecided
            bucket.append((assertions, doc.get("label", ""), identifier))

        rows.append(
            {
                "identifier": identifier,
                "label": doc.get("label", ""),
                "habitat_category": doc.get("habitat_category", ""),
                "grounding_status": doc.get("grounding_status", ""),
                "mapping_status": doc.get("mapping_status", ""),
                "sources": "|".join(sources),
                "source_count": len(sources),
                "assertion_total": assertions,
                "has_definition": bool(doc.get("definition")),
                "n_parents": len(doc.get("parent_habitats") or []),
                "n_parameters": len(doc.get("environmental_parameters") or []),
                "n_taxa": len(doc.get("characteristic_taxa") or []),
                "n_causal_graphs": len(doc.get("causal_graphs") or []),
                "path": str(path.relative_to(REPO_ROOT)),
            }
        )

    table("habitat_category", by_category, total)
    table("grounding_status", by_grounding, total)
    table("mapping_status", by_status, total)
    table("identifier prefix", by_prefix, total)
    table("records attested by each source", by_source, total)
    table("field coverage", field_coverage, total)

    print("\n=== source corroboration ===")
    for n, count in sorted(corroboration.items()):
        print(f"  attested by {n} source(s)  {count:6d}  {100 * count / total:5.1f}%")

    print("\n=== upstream assertions behind the corpus ===")
    print("  (counts are per-source units and are NOT summable across sources)")
    for source, count in sorted(source_totals.items(), key=lambda kv: -kv[1]):
        print(f"  {source:22s} {count:9d}")

    if term_requests:
        term_requests.sort(reverse=True)
        print(f"\n=== ENVO term requests: {len(term_requests)} examined individually ===")
        print("  (a curator read these and confirmed no term fits)")
        for assertions, label, identifier in term_requests[: args.ungrounded_top or len(term_requests)]:
            print(f"  {assertions:8d}  {label[:52]:52s}  {identifier}")

    if class_swept:
        class_swept.sort(reverse=True)
        total_assertions = sum(a for a, _, _ in class_swept)
        print(f"\n=== class-level sweep: {len(class_swept)} ungrounded, {total_assertions} assertions ===")
        print("  (no term matched by any lexical route, but nobody read them one by one —")
        print("   they do NOT count as REVIEWED. `just worklist` ranks them for real curation.)")
        for assertions, label, identifier in class_swept[: args.ungrounded_top]:
            print(f"  {assertions:8d}  {label[:52]:52s}  {identifier}")

    if args.ungrounded_top and undecided:
        undecided.sort(reverse=True)
        print(f"\n=== top {args.ungrounded_top} wholly UNDECIDED ungrounded records ===")
        for assertions, label, identifier in undecided[: args.ungrounded_top]:
            print(f"  {assertions:8d}  {label[:52]:52s}  {identifier}")

    cohorts, risky_total, cohort_backlog = _mapping_cohorts(item_decided)
    if cohorts:
        total_mapped = sum(cohorts[c] for c in COHORTS)
        print(f"\n=== {total_mapped} upstream mappings, by how the object label relates "
              "to the subject ===")
        print("  (the seeder checks object_id against object_label; it is blind by")
        print("   construction when those agree and the mapping itself is wrong)")
        for cohort, why in COHORTS.items():
            marker = "  <-" if cohort in RISK_COHORTS else "    "
            print(f"  {cohort:12s} {cohorts.get(cohort, 0):5d}{marker} {why}")

    if cohort_backlog and args.ungrounded_top:
        identity = sum(1 for row in cohort_backlog if row[0])
        shown = min(args.ungrounded_top, len(cohort_backlog))
        print(f"\n=== {len(cohort_backlog)} of {risky_total} risky mappings still "
              "undecided ===")
        print(f"  ({identity} would become a record's identity and rank first; the rest are")
        print("   kept only as an xref. The gap to the cohort total is rows already decided")
        print("   per-item, or naming a subject neither BacDive nor GOLD brings into this")
        print(f"   corpus. Volume is strains for BacDive, assertions for GOLD. Showing {shown}.)")
        for is_identity, strains, cohort, subject, target, label, identifier in (
            cohort_backlog[: args.ungrounded_top]
        ):
            flag = "id " if is_identity else "   "
            print(f"  {flag}{strains:7d}  {cohort:8s} {subject[:26]:26s} -> {target:18s} "
                  f"{label[:26]:26s} {identifier}")

    # The same idea one level in: not what upstream mapped, but what the
    # seeder's own lexical routes grounded (#62).
    grounding_counts: Counter = Counter()
    grounding_backlog: list[tuple] = []
    for _, doc in records:
        identifier = doc.get("identifier", "")
        if identifier.startswith("habitatmech:"):
            continue  # minted: nothing was claimed, so nothing to check
        for attestation in doc.get("source_attestations") or []:
            source_label = attestation.get("source_label") or ""
            cohort = grounding_cohort(
                source_label, doc.get("label", ""), attestation.get("source_path") or "")
            grounding_counts[cohort] += 1
            if cohort in GROUNDING_RISK and doc.get("mapping_status") != "REVIEWED":
                grounding_backlog.append((
                    attestation.get("assertion_count") or 0, cohort, source_label,
                    identifier, doc.get("label", ""),
                ))
    if grounding_counts:
        total_att = sum(grounding_counts[c] for c in GROUNDING_COHORTS)
        print(f"\n=== {total_att} groundings, by how the record's label relates "
              "to its source's ===")
        print("  (the seeder grounds on ontology SYNONYMS too, and a synonym is")
        print("   ambiguous across domains — nothing else checks this route)")
        for cohort, why in GROUNDING_COHORTS.items():
            marker = "  <-" if cohort in GROUNDING_RISK else "    "
            print(f"  {cohort:10s} {grounding_counts.get(cohort, 0):6d}{marker} {why}")

    if args.ungrounded_top:
        # Printed even when empty, like the screens below it. A section that
        # disappears once it is clean reads as "not run" rather than "nothing
        # to report", and this is the cohort whose emptiness is the result.
        grounding_backlog.sort(reverse=True)
        print(f"\n=== {len(grounding_backlog)} risky groundings not yet reviewed ===")
        for assertions, cohort, source_label, identifier, label in (
            grounding_backlog[: args.ungrounded_top]
        ):
            print(f"  {assertions:7d}  {cohort:8s} {source_label[:24]:24s} -> "
                  f"{label[:32]:32s} {identifier}")
        if not grounding_backlog:
            print("  none — every disjoint or narrowed grounding has been read")

    stale = _stale_class_sweeps(class_swept_ids, records)
    print(f"\n=== {len(stale)} class-level sweep(s) the slice has since contradicted ===")
    print("  (re-tested with propose_decisions.classify — the same function the sweep")
    print("   used — so the claim is checked by the code that made it. Vendoring an")
    print("   ontology makes that negative stale and nothing else re-checks it.)")
    for assertions, label, found, identifier in stale[: args.ungrounded_top or None]:
        print(f"  {assertions:8d}  {label[:28]:28s} -> {found:18s} {identifier}")
    if not stale:
        print("  none — every sweep still lands in the tier it claimed")

    nonhab = _non_habitat_candidates(class_swept_ids, records)
    if _kg_microbe_ontologies() is None:
        print("\n=== swept concepts that may not be habitats: not checked ===")
        print("  (needs a kg-microbe checkout for the non-habitat ontologies; set")
        print("   KG_MICROBE_ROOT or conf/sources.yaml. Absent here, so this is unknown,")
        print("   not clean.)")
    else:
        print(f"\n=== {len(nonhab)} swept concept(s) whose label names a non-habitat ===")
        print("  (a class-level sweep says outright that whether the concept is a habitat")
        print("   at all was NOT assessed. This asks that question against the ontologies")
        print("   that exist to name chemicals, organisms, qualities and diseases. It")
        print("   RANKS — the path overturns roughly half: \"White\" under Muscles is white")
        print("   muscle tissue, not PATO's *white*.)")
        for assertions, label, kind, term_id, identifier in nonhab[: args.ungrounded_top or None]:
            print(f"  {assertions:7d}  {label[:24]:24s} = {kind:32s} {term_id:16s} {identifier}")
        if not nonhab:
            print("  none — no swept concept's label names a chemical, organism or quality")

    same_as = _same_as_candidates(records)
    print(f"\n=== {len(same_as)} novel label(s) held by records from different sources ===")
    print("  (nothing merges two concepts unless they share an ONTOLOGY term, so two")
    print("   sources naming one habitat nothing names produce two permanent records.")
    print("   A shared label is evidence, not proof — decide with SAME_AS after reading.)")
    for volume, label, members in same_as[: args.ungrounded_top or None]:
        print(f"  {volume:7d}  {label[:34]:34s} "
              f"{[(i.split('.')[0].replace('habitatmech:', ''), v) for i, _s, v in members]}")
    if not same_as:
        print("  none — no novel label is shared across sources")

    triad_review = _triad_inventory_review()
    missing_triads = triad_review["missing"]
    organism_triads = triad_review["organism"]
    label_mismatches = triad_review["label_mismatch"]
    if missing_triads or organism_triads or label_mismatches:
        print("\n=== GOLD triad inventory compatibility ===")
        rejected_triads = [*missing_triads, *organism_triads]
        if rejected_triads:
            rejected_paths = {row["canonical_path"] for row in rejected_triads}
            print(
                f"  {len(rejected_triads)} rejected slot(s) across "
                f"{len(rejected_paths)} path(s)"
            )
        if missing_triads:
            missing_terms = {row["top_term"] for row in missing_triads}
            missing_prefixes = Counter(
                term.partition(":")[0] for term in missing_terms
            )
            print(
                f"  {len(missing_triads)} slot(s), {len(missing_terms)} term(s) "
                "are absent from the vendored slice and excluded"
            )
            print(
                "  missing prefixes: "
                + ", ".join(
                    f"{prefix}={count}"
                    for prefix, count in sorted(missing_prefixes.items())
                )
            )
            obsolete = sorted(
                {
                    (row["top_term"], row["top_label"])
                    for row in missing_triads
                    if "obsolete" in row["top_label"].lower()
                }
            )
            for term, label in obsolete:
                print(f"  upstream obsolete annotation: {term} {label}")
        if organism_triads:
            organism_terms = {row["top_term"] for row in organism_triads}
            print(
                f"  {len(organism_triads)} slot(s), {len(organism_terms)} "
                "organism-like/taxon-valued term(s) are invalid as habitat "
                "identities and excluded"
            )
        if label_mismatches:
            mismatch_terms = _distinct_triad_label_mismatches(label_mismatches)
            mismatch_term_count = len({term for term, _gold, _slice in mismatch_terms})
            print(
                f"  {len(label_mismatches)} slot(s), {mismatch_term_count} term(s) "
                "have cached GOLD labels that disagree with the vendored slice; "
                "the slice label is authoritative"
            )
            for term, gold_label, slice_label in mismatch_terms:
                print(
                    f"  label mismatch: {term} GOLD={gold_label!r} "
                    f"slice={slice_label!r}"
                )

    triads = _triad_evidence(records, triad_review)
    slice_labels = _slice_term_labels()
    if triads:
        strong = [t for t in triads if t[0] >= 1]
        print(f"\n=== {len(triads)} minted record(s) whose GOLD path carries an ENVO triad ===")
        print("  (what the submitters said the environment was, which is a different kind of")
        print("   evidence from a label match. Ranked by INDEPENDENT studies agreeing, not")
        print("   samples: of 140 paths where every sample agrees, 122 are one study repeating")
        print("   itself. Ranks; a triad is three terms and which is the identity is a")
        print("   judgement.)")
        print(f"  {len(strong)} have at least one slot corroborated by 2+ studies")
        for corrob, studies, label, path, identifier, slots in triads[: args.ungrounded_top or None]:
            if not corrob:
                continue
            print(f"  [{corrob}/3 corroborated, {studies} studies]  {label[:24]:24s} {identifier}")
            print(f"       path: {path[:70]}")
            for slot in ("broad", "local", "medium"):
                row = slots.get(slot)
                if row:
                    # The slice's label, not GOLD's cached one: four of GOLD's
                    # are stale (agricultural feature -> agricultural
                    # ecosystem), and a curator copying the wrong one into a
                    # decision gets a hard seed failure (#131).
                    label = row.get("slice_label") or slice_labels.get(
                        row["top_term"], row["top_label"]
                    )
                    print(f"       {slot:6s} {row['top_term']:16s} {label[:28]:28s} "
                          f"share={row['top_share']} studies={row['studies_agreeing']}")

    kinds, kind_assertions = _coverage_over_ontologies(records)
    total = sum(kinds.values())
    new_over_envo = total - kinds["named_by_envo"]
    novel = kinds["unnamed"] + kinds["refines_envo"] + kinds["refines_other"]
    print("\n=== what HabitatMech adds over the ontologies it grounds to ===")
    for key, why in COVERAGE_KINDS:
        print(f"  {kinds[key]:5d} ({100 * kinds[key] / total:4.1f}%)  "
              f"{kind_assertions[key]:7d} assertions   {why}")
    print(f"\n  new over ENVO:              {new_over_envo:5d} of {total} "
          f"({100 * new_over_envo / total:.1f}%) — concepts ENVO has no term for")
    print(f"  new over every vendored OBO:{novel:6d} of {total} "
          f"({100 * novel / total:.1f}%) — HabitatMech supplies the label and definition")
    print("  (a concept that merely hangs UNDER an ENVO term counts as new: the")
    print("   ambiguous-leaf rule mints an id precisely because the matched term is")
    print("   broader, so ENVO naming the parent is not ENVO naming the concept.)")

    compound = _compound_path_candidates(class_swept_ids, records)
    print(f"\n=== {len(compound)} swept concept(s) whose PATH names a term the leaf does not ===")
    print("  (every search route reads the leaf alone, but a GOLD leaf is the last step")
    print("   of a path: \"Hyaline\" under Cartilage is hyaline cartilage, and on its own")
    print("   it finds PATO's *transparent*. Ranks candidates; each still needs reading.)")
    for assertions, path, term_id, label, identifier in compound[: args.ungrounded_top or None]:
        print(f"  {assertions:8d}  {path[:30]:30s} -> {term_id:16s} {label[:28]:28s} {identifier}")
    if not compound:
        print("  none — no swept concept's parent+leaf compound matches a habitat term")

    try:
        from habitatmech.sampling import recorded_samples
        samples = recorded_samples()
    except ImportError:
        samples = []
    if samples:
        print("\n=== sampled slices: what has been measured rather than read ===")
        print("  (slices too large to review one by one. The draw and the verdicts are")
        print("   committed under curation/samples/, so the rate is auditable, and the")
        print("   interval is Wilson — the normal approximation puts the lower bound")
        print("   below zero at these counts.)")
        # "wrong" is not the same claim in every slice, and reading it as one
        # makes 175 non-habitats look like 175 defects.
        MEANS = {
            "CLASS_SWEPT_UNSCREENED": "not a habitat at all, so NOT_APPLICABLE rather "
                                      "than a term request",
        }
        for s in samples:
            low, high = s["interval"]
            gloss = MEANS.get(s["grounding"], "a defective grounding")
            print(f"  [{s['grounding']}] a defect here means: {gloss}")
            print(f"  {s['grounding']:10s} {s['wrong']}/{s['judged']} wrong "
                  f"= {100 * s['wrong'] / s['judged'] if s['judged'] else 0:.1f}%, "
                  f"95% CI {100 * low:.1f}-{100 * high:.1f}%  "
                  f"-> at most {high * s['population']:.0f} of {s['population']} unreviewed")
            if s["unparsed"]:
                print(f"    {s['unparsed']} verdict(s) not understood and excluded — "
                      "the rate above is over the rest")

    organism = _organism_identities(records)
    print(f"\n=== {len(organism)} record(s) claiming a non-habitat is a habitat ===")
    print("  (an organism or a process, which MIxS rules out of the environmental")
    print("   triad in one sentence. A label match cannot see this — ")
    print("   NCIT:C77916 really is labelled Protozoa — so it is asked of the")
    print("   ontology's own ancestry instead, vendored by #46.)")
    for assertions, identifier, label, where in organism[: args.ungrounded_top or None]:
        print(f"  {assertions:8d}  [{where:8s}] {label[:44]:44s} {identifier}")
    if not organism:
        print("  none — the class is currently empty, and stays visible if it refills")

    unverifiable = _unverifiable_mapping_targets()
    if unverifiable:
        print(f"\n=== {len(unverifiable)} upstream mapping target(s) that cannot be label-checked ===")
        print("  (their ontology is not vendored, so a wrong id here would not be caught;")
        print("   upstream has a measured error rate on the rows that CAN be checked)")
        for subject, target, claimed, identity in unverifiable:
            flag = "  <- can be a record identity" if identity else ""
            print(f"  {subject[:26]:26s} {target:18s} claims {claimed!r}{flag}")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(sorted(rows, key=lambda r: r["identifier"]))
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
