from unittest import TestCase
from src.ChangelogEntry import ChangelogEntry


class TestChangelogEntry(TestCase):
    def setUp(self) -> None:
        self.changelogEntry = ChangelogEntry('woocommerce', 'v3.2.1')

    def test_get_changelog_entries(self):
        self.assertEqual(self.changelogEntry.get_changelog_entries(), ['Fix archive size for partners', 'test1', 'test2'])
