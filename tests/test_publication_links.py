"""Regression checks for DOI buttons, independent of publisher availability."""

import importlib.util
from pathlib import Path
import unittest


spec = importlib.util.spec_from_file_location(
    "publication_audit", Path(__file__).resolve().parents[1] / "scripts/audit-publications.py"
)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


def button(href, text="DOI"):
    link = audit.Node("a", [("href", href)])
    link.children.append(text)
    return link


class DoiLinksTest(unittest.TestCase):
    def test_accepts_bare_identifiers_behind_one_resolver(self):
        for identifier in ["10.1002/adma.201870214", "10.1021/acs.chemmater.0c01187",
                           "10.1002/smll.201670244", "10.26434/chemrxiv-2021-6617l"]:
            with self.subTest(identifier=identifier):
                audit.validate_doi_links(button("https://doi.org/" + identifier), "fixture")

    def test_rejects_url_in_doi_and_malformed_resolvers(self):
        for href in ["https://doi.org/https://doi.org/10.1002/smll.201601630",
                     "https://doi.org/https://aiche.confex.com/aiche/2020/meetingapp.cgi/Paper/605068",
                     "https://doi.org/https%3A%2F%2Fdoi.org%2F10.1002%2Ftest",
                     "https://doi.org/10.1002/has%20spaces", "https://doi.org/",
                     "http://doi.org/10.1002/test", "https://doi.org.example/10.1002/test"]:
            with self.subTest(href=href), self.assertRaises(SystemExit):
                audit.validate_doi_links(button(href), "fixture")

    def test_non_doi_links_remain_valid_separate_destinations(self):
        audit.validate_doi_links(button(
            "https://aiche.confex.com/aiche/2020/webprogram/Paper605068.html", "Conference abstract"
        ), "fixture")
        audit.validate_doi_links(audit.Node(), "record without DOI")


if __name__ == "__main__":
    unittest.main()
