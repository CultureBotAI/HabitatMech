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
