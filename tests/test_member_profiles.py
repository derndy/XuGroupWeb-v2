"""Unit tests for generated member-profile auditing helpers."""

import importlib.util
from pathlib import Path
import tempfile
import unittest


spec = importlib.util.spec_from_file_location(
    "member_profile_audit", Path(__file__).resolve().parents[1] / "scripts/audit-member-profiles.py"
)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class MemberProfileAuditTest(unittest.TestCase):
    def test_parser_preserves_classes_and_accessible_names(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "profile.html"
            fixture.write_text(
                '<main class="person-profile" aria-labelledby="person-name">'
                '<h1 id="person-name">Example Member</h1>'
                '<a href="#collaboration">Collaborate</a>'
                '<section id="collaboration"></section></main>',
                encoding="utf-8",
            )
            document = audit.Document(fixture).root
            profile = audit.validate_landmarks_and_references(document, fixture)
            self.assertEqual(audit.normalized(profile.find(lambda node: node.tag == "h1")[0]),
                             "Example Member")

    def test_broken_internal_anchor_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "profile.html"
            fixture.write_text(
                '<main class="person-profile" aria-labelledby="person-name">'
                '<h1 id="person-name">Example Member</h1>'
                '<a href="#missing">Missing target</a></main>',
                encoding="utf-8",
            )
            with self.assertRaises(SystemExit):
                audit.validate_landmarks_and_references(audit.Document(fixture).root, fixture)


if __name__ == "__main__":
    unittest.main()
