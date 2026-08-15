"""The committed data/raw inventories are the seeder's only input.

They are derived data, but they are checked in, which means they can drift from
what the extractor would produce today. These tests check the shape and
internal consistency a reader (and the seeder) relies on.
"""

from __future__ import annotations

import re

import yaml

EXPECTED_COLUMNS = {
    "gold_ecosystem_paths.tsv": {
        "canonical_path", "ecosystem", "ecosystem_category", "ecosystem_type",
        "ecosystem_subtype", "specific_ecosystem", "leaf_label", "depth",
        "gold_node_count", "organism_count", "total_assertions", "gold_node_ids",
    },
    "bacdive_isolation_sources.tsv": {"bacdive_id", "label", "source_slug", "strain_count"},
    "prego_habitats.tsv": {"prego_id", "ontology", "taxon_count", "max_prego_score"},
    "prego_habitat_taxa.tsv": {"prego_id", "rank", "taxon_id", "taxon_label", "prego_score"},
    "environment_parameters.tsv": {"main_group", "env_type", "parameter", "value", "term_ids"},
    "isolation_source_groundings.tsv": {"subject_label", "object_id", "object_source", "predicate_id"},
    "ontology_terms.tsv": {"term_id", "ontology", "label", "definition", "synonyms"},
    "ontology_subclass_edges.tsv": {"subject", "predicate", "object"},
}


def test_every_inventory_has_its_expected_columns(raw_tsv):
    for name, expected in EXPECTED_COLUMNS.items():
        rows = raw_tsv(name)
        assert rows, f"{name} is empty"
        missing = expected - set(rows[0])
        assert not missing, f"{name} missing columns: {sorted(missing)}"


def test_manifest_row_counts_match_the_files(repo_root, raw_tsv):
    """The manifest is what a reader trusts to know the inventories are a
    coherent set. A count that disagrees with the file means someone
    regenerated one TSV without the others."""
    manifest_path = repo_root / "data" / "raw" / "MANIFEST.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    for output in manifest["outputs"]:
        name = output["path"]
        if name not in EXPECTED_COLUMNS:
            continue
        assert len(raw_tsv(name)) == output["rows"], f"{name}: manifest says {output['rows']}"


def test_gold_paths_are_unique(raw_tsv):
    """The canonical path IS the GOLD concept's identity — the seeder mints
    identifiers from it. A duplicate means two concepts would collide onto one
    minted id and the second would overwrite the first."""
    paths = [r["canonical_path"] for r in raw_tsv("gold_ecosystem_paths.tsv")]
    assert len(paths) == len(set(paths))


def test_gold_depth_matches_the_path(raw_tsv):
    bad = [
        r["canonical_path"]
        for r in raw_tsv("gold_ecosystem_paths.tsv")
        if int(r["depth"]) != len(r["canonical_path"].split(" > "))
    ]
    assert not bad, f"depth disagrees with canonical_path: {bad[:5]}"


def test_gold_paths_carry_no_unclassified_filler(raw_tsv):
    """"Unclassified" is GOLD's no-value-at-this-level filler. A trailing one
    would create a spurious concept ("Soil > Unclassified") distinct from the
    real one."""
    bad = [
        r["canonical_path"]
        for r in raw_tsv("gold_ecosystem_paths.tsv")
        if r["canonical_path"].endswith("Unclassified")
    ]
    assert not bad, f"paths ending in the Unclassified filler: {bad[:5]}"


def test_gold_leaf_label_is_the_last_path_element(raw_tsv):
    bad = [
        r["canonical_path"]
        for r in raw_tsv("gold_ecosystem_paths.tsv")
        if r["leaf_label"] != r["canonical_path"].split(" > ")[-1]
    ]
    assert not bad, f"leaf_label disagrees with the path: {bad[:5]}"


def test_bacdive_ids_are_unique(raw_tsv):
    ids = [r["bacdive_id"] for r in raw_tsv("bacdive_isolation_sources.tsv")]
    assert len(ids) == len(set(ids))


def test_every_bacdive_source_has_a_grounding_row(raw_tsv):
    """The seeder's BacDive route depends on this being total. A source with no
    row would fall through to `bacdive_unmapped`, which should never happen
    with kg-microbe's current mapping table — if it starts happening, the
    table has drifted and the seeder is silently degrading."""
    def norm(text: str) -> str:
        return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()

    keys = set()
    for row in raw_tsv("isolation_source_groundings.tsv"):
        keys.add(norm(row["subject_label"]))
        keys.add(norm(row["subject_label_normalized"]))
    missing = [
        r["label"]
        for r in raw_tsv("bacdive_isolation_sources.tsv")
        if norm(r["label"]) not in keys and norm(r["source_slug"]) not in keys
    ]
    assert not missing, f"BacDive sources with no grounding row: {missing[:10]}"


def test_prego_ids_are_ontology_curies(raw_tsv):
    bad = [r["prego_id"] for r in raw_tsv("prego_habitats.tsv")
           if not r["prego_id"].startswith(("ENVO:", "BTO:"))]
    assert not bad, f"unexpected PREGO habitat prefixes: {bad[:10]}"


def test_prego_taxa_reference_known_habitats(raw_tsv):
    habitats = {r["prego_id"] for r in raw_tsv("prego_habitats.tsv")}
    orphans = {r["prego_id"] for r in raw_tsv("prego_habitat_taxa.tsv")} - habitats
    assert not orphans, f"taxa rows for unknown habitats: {sorted(orphans)[:10]}"


def test_prego_taxa_respect_the_per_habitat_cap(raw_tsv):
    """The extractor keeps a bounded number of taxa per habitat. If this grows
    unbounded the corpus does too — PREGO asserts ~8700 taxa for soil alone."""
    counts: dict[str, int] = {}
    for row in raw_tsv("prego_habitat_taxa.tsv"):
        counts[row["prego_id"]] = counts.get(row["prego_id"], 0) + 1
    assert max(counts.values()) <= 25


def test_ontology_subclass_edges_stay_inside_the_slice(raw_tsv):
    """The vendored hierarchy must be self-contained; a dangling parent means
    the seeder's ancestor walk silently stops early and categorisation by ENVO
    anchor gets the wrong answer."""
    terms = {r["term_id"] for r in raw_tsv("ontology_terms.tsv")}
    edges = raw_tsv("ontology_subclass_edges.tsv")
    dangling = [
        (e["subject"], e["object"])
        for e in edges
        if e["subject"] not in terms or e["object"] not in terms
    ]
    assert not dangling, f"subclass edges leaving the slice: {dangling[:10]}"


def test_ontology_terms_are_unique(raw_tsv):
    ids = [r["term_id"] for r in raw_tsv("ontology_terms.tsv")]
    assert len(ids) == len(set(ids))


def test_environment_parameter_term_ids_are_curies(raw_tsv):
    """The column is `term_ids`, not `envo_ids`, deliberately: upstream's
    ENVO_ids cell also carries PATO qualifiers (`sediment_marine_cold`),
    UBERON anatomy (`milk`), FOODON, CHEBI, and NCBITaxon. Asserting an ENVO
    prefix here would encode a false assumption that 149 rows violate."""
    curie = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+$")
    bad = []
    for row in raw_tsv("environment_parameters.tsv"):
        for term in (row["term_ids"] or "").split("|"):
            if term and not curie.match(term):
                bad.append(term)
    assert not bad, f"malformed term ids in the parameter table: {bad[:10]}"


def test_mesh_dump_is_found_by_glob_not_by_pinned_year(tmp_path, capsys):
    """The MeSH dump is named for its release (`mesh2026.nt.gz`), so pinning the
    year would make the next refresh a silent no-op: the label check would stop
    running on MeSH targets and nothing would say so (#45)."""
    import gzip
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
    import extract_source_inventory as extract

    raw = tmp_path / "data" / "raw"
    raw.mkdir(parents=True)
    for year, label in (("2026", "Stale"), ("2031", "Abscess")):
        with gzip.open(raw / f"mesh{year}.nt.gz", "wt", encoding="utf-8") as fh:
            fh.write(
                f"<http://id.nlm.nih.gov/mesh/{year}/D000038> "
                f'<http://www.w3.org/2000/01/rdf-schema#label> "{label}"@en .\n'
            )

    # The newest release wins, and a year nobody hardcoded still resolves.
    assert extract._reference_labels(tmp_path, {"mesh:D000038"}) == {"mesh:D000038": "Abscess"}


def test_a_missing_reference_source_warns_instead_of_degrading_silently(tmp_path, capsys):
    """Every reference source is optional, so a missing one leaves the target
    unverifiable rather than failing the run. That is the right behaviour and
    the wrong thing to leave silent — it is indistinguishable from upstream not
    using the ontology at all (#45)."""
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
    import extract_source_inventory as extract

    (tmp_path / "data" / "raw").mkdir(parents=True)
    assert extract._reference_labels(tmp_path, {"NCIT:C17649"}) == {}
    out = capsys.readouterr().out
    assert "WARNING" in out and "NCIT" in out and "ncit.db" in out


def test_label_cohorts_separate_the_defect_class_the_seeder_cannot_see():
    """The seeder checks an upstream mapping's object_id against its
    object_label, so it is blind by construction when those agree and the
    mapping itself is wrong. The cohorts rank that second class: a target whose
    label is a strict subset of the subject's words dropped modifiers
    (`Cooling-tower` -> Tower), and one sharing no word was matched on a
    synonym, where over-narrowing hides (`Reptilia` -> Lepidosauria).

    It ranks, it does not decide — half the subset cohort is correct, because
    the subject is an enumeration and dropping an alternative is right."""
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
    from habitat_report import label_cohort

    assert label_cohort("abscess", "Abscess") == "identical"
    assert label_cohort("cooling tower", "Tower") == "subset"
    assert label_cohort("feces stool", "feces") == "subset"       # dropped, correctly
    assert label_cohort("chicken", "Gallus gallus") == "disjoint"
    # Tokenization artefacts, not mapping defects: same letters, different
    # spacing or an inflectional tail. Flagging these buried the real findings
    # under repeats of "Composting" once GOLD's route was joined (#52).
    assert label_cohort("wastewater", "waste water") == "identical"
    assert label_cohort("composting", "compost") == "identical"
    assert label_cohort("clean room", "cleanroom") == "identical"
    # ...but the narrowness has to hold: a dropped word that IS the meaning
    # must still be caught.
    assert label_cohort("cooling tower", "Tower") == "subset"
    assert label_cohort("plant factory", "factory") == "subset"
    assert label_cohort("acid mine drainage", "acid mine drainage site") == "overlap"
    # The known false negative, stated rather than hidden: "sample" is shared,
    # so a plainly wrong mapping lands in the low-risk bucket.
    assert label_cohort("core sample", "Nucleotide Sequence Sample Name") == "overlap"


def test_madin_taxa_carry_no_invented_rank_or_score(raw_tsv):
    """Madin supplies neither a rank nor a score. The extractor must not
    manufacture one — a `rank` column filled with the sort order reads as a
    ranking that does not exist, and #8 established that this corpus reports
    what a source actually says rather than what would be convenient (#40)."""
    rows = list(raw_tsv("madin_habitat_taxa.tsv"))
    assert rows, "no Madin taxa extracted"
    assert set(rows[0]) == {"madin_id", "taxon_id", "taxon_label", "corroborated_by"}


def test_madin_bacdive_vocabulary_rows_are_addressable(raw_tsv):
    """Five Madin habitats are `bacdive.isolation_source:` ids, and they are
    keyed under BACDIVE so that a BacDive extraction reaching the compound level
    would merge with them rather than duplicate them. None overlap today —
    Madin uses the compound paths (`host_animal_endotherm`), kg-microbe's
    BacDive transform emits single tokens (`host`) — so the thing that actually
    has to hold is that every one of them can still be addressed by a curation
    decision (#40)."""
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
    from seed_from_sources import _madin_key, mint

    shared = [
        r["madin_id"] for r in raw_tsv("madin_habitats.tsv")
        if r["madin_id"].startswith("bacdive.isolation_source:")
    ]
    assert shared, "expected Madin habitats in the BacDive vocabulary"
    assert all(_madin_key(m) == mint("BACDIVE", m) for m in shared)
    assert all(_madin_key(m).startswith("habitatmech:BACDIVE.") for m in shared)


def test_environment_table_decision_survives_another_source_attesting_the_term():
    """A curator's decision on an environment-table row must hold regardless of
    what else attested the same term. Consulting `apply_decision` only when no
    concept existed meant the ruling held until some other source happened to
    attest that term and then silently stopped — Madin self-grounding
    UBERON:0000468 deleted the record ruled NOT_APPLICABLE and replaced it with
    the EXACT one the curator had refused, with nothing failing (#56)."""
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
    import seed_from_sources as seed

    corpus = seed.build_corpus()
    by_id = {c.identifier: c for c in corpus.concepts}

    ruled_out = {
        d.identifier for d in seed.load_decisions(seed.DECISIONS_PATH).values()
        if d.decision == "NOT_APPLICABLE" and d.identifier.startswith("habitatmech:ENVIRONMENTS_TABLE.")
    }
    assert ruled_out, "expected at least one NOT_APPLICABLE environment-table decision"
    missing = [i for i in ruled_out if i not in by_id]
    assert not missing, (
        f"decisions ruled these NOT_APPLICABLE but no concept carries the minted id: {missing}. "
        "The decision stopped applying — another source now attests the term it names."
    )
    for identifier in ruled_out:
        assert by_id[identifier].grounding_status == "NOT_APPLICABLE"


def test_narrowed_grounding_is_forgiven_when_the_path_already_said_it():
    """"Sediment" grounded to "marine sediment" looks like the record claiming
    specificity the source never had — until you see GOLD's path is
    Environmental > Aquatic > Marine > Sediment. Checking the path is what
    separates a real over-narrowing from the seeder correctly using the context
    it was handed, and it cut this cohort from 67 to 30 (#67)."""
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
    from habitat_report import grounding_cohort

    assert grounding_cohort("Sediment", "marine sediment") == "narrowed"
    assert grounding_cohort(
        "Sediment", "marine sediment", "Environmental > Aquatic > Marine > Sediment"
    ) == "same"
    # A head noun the ontology adds by convention narrows nothing, path or not.
    assert grounding_cohort("Laboratory", "laboratory facility") == "same"
    assert grounding_cohort("Volcanic", "volcanic feature") == "same"
    # ...but a real added modifier the path does not support must still show.
    assert grounding_cohort(
        "Raw milk", "cow milk (raw)", "Engineered > Food production > Dairy products > Raw milk"
    ) == "narrowed"


def test_the_organism_screen_still_detects_a_known_taxon():
    """A screen that returns nothing because it is broken looks exactly like
    one that returns nothing because the corpus is clean — and this one returns
    nothing today. So pin both directions against terms whose answer is known:
    NCIT:C77916 "Protozoa" reaches Organism, NCIT:C17649 "Other" does not (#46)."""
    import csv
    import sys
    from collections import defaultdict
    from pathlib import Path

    root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(root / "scripts"))
    from habitat_report import ORGANISM_ROOTS, _ancestors

    parents = defaultdict(list)
    with (root / "data" / "raw" / "ontology_subclass_edges.tsv").open(
        newline="", encoding="utf-8"
    ) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            parents[row["subject"]].append(row["object"])

    assert _ancestors("NCIT:C77916", parents) & ORGANISM_ROOTS, (
        "Protozoa no longer reaches an organism root — the vendored ancestry has "
        "regressed and the screen is silently answering 'clean' for everything"
    )
    assert _ancestors("mesh:D044003", parents) & ORGANISM_ROOTS, "Sphagnopsida is a plant"
    assert not _ancestors("NCIT:C17649", parents) & ORGANISM_ROOTS, (
        "NCIT 'Other' is a qualifier, not an organism — the screen is over-reporting"
    )


def test_no_decision_grounds_onto_a_term_with_no_place_in_a_hierarchy(raw_tsv):
    """A record grounded onto a bare label has no parents and no siblings. The
    slice marks those rows explicitly rather than leaving them to be inferred
    from a missing subclass edge — 2444 fully vendored terms have none either,
    because they are leaves or their parents fell outside the slice (#46)."""
    import csv
    from pathlib import Path

    root = Path(__file__).resolve().parent.parent
    label_only = {
        r["term_id"] for r in raw_tsv("ontology_terms.tsv") if r.get("label_only") == "TRUE"
    }
    assert label_only, "nothing marked label_only; the marker is not being written"
    with (root / "curation" / "decisions.tsv").open(newline="", encoding="utf-8") as fh:
        offenders = [
            (r["identifier"], r["object_id"])
            for r in csv.DictReader(fh, delimiter="\t")
            if r["decision"] in ("GROUND", "GROUND_AS_PARENT") and r["object_id"] in label_only
        ]
    assert not offenders, f"groundings onto an unplaced term: {offenders[:5]}"


def test_the_drift_guard_compares_by_role_not_by_staged_path():
    """The mapping table is recorded under its role however it was staged, so
    the comparison survives switching between reading it from the checkout and
    pinning it with --mappings. Keying on the staged path meant the two runs
    recorded different names, the lookup found nothing, and the guard passed
    silently — which is how it failed the first time (#72)."""
    import sys
    from pathlib import Path

    root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(root / "scripts"))
    from extract_source_inventory import MAPPINGS_ROLE, _manifest_inputs

    fake = root / "conf"  # any real directory; only the naming is under test
    staged = root / "conf" / "sources.yaml"
    names_unpinned = {name for name, _ in _manifest_inputs(fake, None)}
    names_pinned = {name for name, _ in _manifest_inputs(fake, staged)}
    assert MAPPINGS_ROLE in names_pinned, "a pinned table must still record its role"
    # The only difference between the two may be which files happened to exist,
    # never the NAME the mapping table is recorded under.
    assert names_pinned - names_unpinned <= {MAPPINGS_ROLE}
    pinned = dict(_manifest_inputs(fake, staged))
    assert pinned[MAPPINGS_ROLE] == staged, "the role must point at the staged file"


def test_manifest_records_every_input_it_hashes(raw_tsv):
    """The drift guard compares what the manifest recorded, so an input that is
    read but not recorded is one the guard can never notice changing (#72)."""
    import re
    from pathlib import Path

    manifest = (Path(__file__).resolve().parent.parent / "data" / "raw" / "MANIFEST.yaml")
    text = manifest.read_text(encoding="utf-8")
    paths = re.findall(r"^\s+- path: (.+)$", text, re.M)
    inputs = [p for p in paths if "/" in p]
    assert inputs, "manifest lists no inputs"
    hashed = len(re.findall(r"^\s+sha256: (?!skipped)", text, re.M))
    assert hashed == len(inputs), (
        f"{len(inputs)} inputs recorded but {hashed} carry a real sha256; "
        "an unhashed input is invisible to the drift guard"
    )


def test_the_drift_guard_reports_a_vanished_input_and_an_uncheckable_one(tmp_path, capsys):
    """Two ways for a guard to stop guarding without saying so (#76):

    an input the manifest recorded that the checkout no longer has — filtering
    the input list on exists() hid those entirely, so a source could disappear
    and the extraction would emit a corpus missing it in silence;

    and an input recorded by a --no-hash run, which leaves nothing to compare
    against on every later run. That is the failure #44 already had once."""
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
    from extract_source_inventory import _changed_inputs

    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text(
        "inputs:\n"
        "  - path: gone.tsv\n    sha256: aaa\n"
        "  - path: unhashed.tsv\n    sha256: skipped (--no-hash)\n",
        encoding="utf-8",
    )
    still_here = tmp_path / "unhashed.tsv"
    still_here.write_text("x", encoding="utf-8")

    changed = _changed_inputs(manifest, [("unhashed.tsv", still_here)])
    assert any("MISSING" in c for c in changed), "a vanished input must be reported"
    assert "no recorded sha256" in capsys.readouterr().out, (
        "an uncheckable input must say so rather than passing as unchanged"
    )
