from unittest import TestCase
from src.ChangelogUpdater import ChangelogUpdater


class TestChangelogUpdater(TestCase):
    def setUp(self) -> None:
        self.changelog_updater = ChangelogUpdater('woocommerce', 'v3.2.2', 'v3.2.1', ['7.1', '7.2'],
                                                  ['7.2'], ['3.3.4', '3.8.0'], ['3.8.0'])
        self.changelog_updater_with_platform = ChangelogUpdater('woocommerce', 'v3.2.2', 'v3.2.1', ['7.1', '7.2'],
                                                  ['7.2'], ['3.3.4', '3.8.0'], ['3.8.0'], ['5.0.3', '5.3'], ['5.3'])

    def test_get_compatible_php_versions_table_header_string(self):
        new_table_row = self.changelog_updater.get_compatible_php_versions_table_header_string(
            "|  Overview             "
            "| Woocommerce and Wordpress version                                "
            "| PHP 5.6 | PHP 7.0 | PHP 7.1 | PHP 7.2 |")
        self.assertEqual(new_table_row,
                         "|  Overview             "
                         "| Woocommerce and Wordpress version                                "
                         "| PHP 7.1 | PHP 7.2 |")

    def test_get_tested_php_versions_table_string(self):
        new_table_row = self. \
            changelog_updater. \
            get_tested_php_versions_table_string("| Woocommerce version 3.8.0, Wordpress version 5.3                 "
                                                 "|   :x:   "
                                                 "|   :x:   "
                                                 "|   :x:   "
                                                 "| " + u"\u2705" + " |")
        self.assertEqual(new_table_row,
                         "| Woocommerce version 3.8.0, Wordpress version 5.3                 "
                         "|   :x:   "
                         "| " + u"\u2705" + " |")

    def test_get_compatible_php_versions_table_string(self):
        new_table_row = self. \
            changelog_updater. \
            get_compatible_php_versions_table_string("| Woocommerce version 3.3.4 - 3.8.0, Wordpress version 5.0.3 - "
                                                     "5.3 "
                                                     "| " + u"\u2705" + " "
                                                     "| " + u"\u2705" + " "
                                                     "| " + u"\u2705" + " "
                                                     "| " + u"\u2705" + " |")
        self.assertEqual("| Woocommerce version 3.3.4 - 3.8.0, Wordpress version 5.0.3 - 5.3 "
                         "| " + u"\u2705" + " "
                         "| " + u"\u2705" + " |", new_table_row)

    def test_get_tested_shopsystem_and_platform_versions_table_string_no_platform(self):
        new_table_row = self. \
            changelog_updater. \
            get_tested_shopsystem_and_platform_versions_table_string("| Woocommerce version 1.1.1                 "
                                                                     "|   :x:   "
                                                                     "|   :x:   "
                                                                     "|   :x:   "
                                                                     "| " + u"\u2705" + " |")
        self.assertEqual("| Woocommerce version 3.8.0                 "
                         "|   :x:   "
                         "|   :x:   "
                         "|   :x:   "
                         "| " + u"\u2705" + " |", new_table_row)

    def test_get_compatibility_shopsystem_and_platform_versions_table_string_no_platform(self):
        new_table_row = self. \
            changelog_updater. \
            get_compatibility_shopsystem_and_platform_versions_table_string("| Woocommerce version 1.1.1 - 2.2.2 "
                                                                            "| " + u"\u2705" + " "
                                                                            "| " + u"\u2705" + " "
                                                                            "| " + u"\u2705" + " "
                                                                            "| " + u"\u2705" + " |")
        self.assertEqual("| Woocommerce version 3.3.4 - 3.8.0 "
                         "| " + u"\u2705" + " "
                         "| " + u"\u2705" + " "
                         "| " + u"\u2705" + " "
                         "| " + u"\u2705" + " |", new_table_row)

    def test_get_tested_shopsystem_and_platform_versions_table_string_with_platform(self):
        new_table_row = self. \
            changelog_updater_with_platform. \
            get_tested_shopsystem_and_platform_versions_table_string("| Woocommerce version 1.1.1,"
                                                                     " Wordpress version 2.3                 "
                                                                     "|   :x:   "
                                                                     "|   :x:   "
                                                                     "|   :x:   "
                                                                     "| " + u"\u2705" + " |")
        self.assertEqual("| Woocommerce version 3.8.0, Wordpress version 5.3                 "
                         "|   :x:   "
                         "|   :x:   "
                         "|   :x:   "
                         "| " + u"\u2705" + " |", new_table_row)

    def test_get_compatiblity_shopsystem_and_platform_versions_table_string_with_platform(self):
        new_table_row = self. \
            changelog_updater_with_platform. \
            get_compatibility_shopsystem_and_platform_versions_table_string("| Woocommerce version 1.1.1 - 2.2.2, "
                                                                            "Wordpress version 3.3.3 - 4.4.4 "
                                                                            "| " + u"\u2705" + " "
                                                                            "| " + u"\u2705" + " "
                                                                            "| " + u"\u2705" + " "
                                                                            "| " + u"\u2705" + " |")
        self.assertEqual("| Woocommerce version 3.3.4 - 3.8.0,"
                         " Wordpress version 5.0.3 - 5.3 "
                         "| " + u"\u2705" + " "
                         "| " + u"\u2705" + " "
                         "| " + u"\u2705" + " "
                         "| " + u"\u2705" + " |", new_table_row)

    def test_get_index_of_first_cell_containing_text(self):
        new_table_row = self.changelog_updater.get_row_separator_table_row(
            "|-----------------------"
            "|------------------------------------------------------------------"
            "|:-------:"
            "|:-------:"
            "|:-------:"
            "|:-------:|")
        self.assertEqual(new_table_row,
                         "|-----------------------"
                         "|------------------------------------------------------------------"
                         "|:-------:"
                         "|:-------:|")
