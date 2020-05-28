from unittest import TestCase
from src.ChangelogTableHelper import ChangelogTableHelper


class TestChangelogTableHelper(TestCase):
    def test_get_first_sign_in_table_row_index_with_cross(self):
        self.assertEqual(ChangelogTableHelper.get_first_sign_in_table_row_index(["", ":x:"]), 1)

    def test_get_first_sign_in_table_row_index_with_tick(self):
        self.assertEqual(ChangelogTableHelper.get_first_sign_in_table_row_index(["", "&#9989;"]), 1)

    def test_get_first_sign_in_table_row_index_with_unicode_tick(self):
        self.assertEqual(ChangelogTableHelper.get_first_sign_in_table_row_index(["", u"\u2705"]), 1)

    def test_is_tick_in_string_with_unicode_tick(self):
        self.assertTrue(ChangelogTableHelper.is_tick_in_string("   " + u"\u2705"))

    def test_is_tick_in_string_with_normal_tick(self):
        self.assertTrue(ChangelogTableHelper.is_tick_in_string("     &#9989;     "))
