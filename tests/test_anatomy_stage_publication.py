"""Source URL migrations must not turn a stage xref into habitat equivalence."""

import csv


def test_anatomy_stage_redirects_and_external_stage_xref(repo_root):
    with (repo_root / "data/habitats/RETIRED.tsv").open(newline="") as handle:
        redirects = {r["retired_slug"]: r for r in csv.DictReader(handle, delimiter="\t")}
    for old, new, identifier in [
        ("adenoid-bto-0000777", "nasopharyngeal-tonsil-bto-0004715", "BTO:0004715"),
        ("adult-bto-0001043", "adult-associated-environment-habitatmech-prego-57e0a5faae",
         "habitatmech:PREGO.57e0a5faae"),
    ]:
        assert redirects[old]["current_identifiers"] == identifier
        assert new in (repo_root / "pages/habitats" / f"{old}.html").read_text()
        assert (repo_root / "pages/habitats" / f"{new}.html").is_file()
    html = (repo_root / "pages/habitats" /
            "adult-associated-environment-habitatmech-prego-57e0a5faae.html").read_text()
    assert 'href="http://purl.obolibrary.org/obo/BTO_0001043"' in html
    assert 'href="../habitats/adult-bto-0001043.html"' not in html
