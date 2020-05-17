from unittest import TestCase
from src.InternalFileUpdater import InternalFileUpdater
from src.FileActionHelper import FileActionHelper


class TestInternalFileUpdater(TestCase):
    def setUp(self) -> None:
        self.internal_file_updater = InternalFileUpdater('woocommerce', '3.2.2', '3.2.1', ['7.1', '7.2'],
                                                         ['7.2'], ['3.3.5', '3.8.0'], ['3.8.1'])
        self.internal_file_updater_with_platform = InternalFileUpdater('woocommerce', '3.2.2', '3.2.1', ['7.1', '7.2'],
                                                                       ['7.2'], ['3.3.4', '3.8.0'], ['3.8.0'],
                                                                       ['5.0.3', '5.3'], ['5.3'])

    def test_get_updated_internal_file_lines_woocommerce_php_file(self):
        file_lines = [" * Version: 3.2.1",
                      " * WC requires at least: 3.3.4",
                      " * WC tested up to: 3.8.0"]
        shop_extension_file_list = FileActionHelper.get_data_from_internal_files()['woocommerce']
        replace_hint_entries = shop_extension_file_list["woocommerce-wirecard-payment-gateway.php"]
        new_lines = self.internal_file_updater.get_updated_internal_file_lines(file_lines, replace_hint_entries)
        self.assertEqual([" * Version: 3.2.2",
                          " * WC requires at least: 3.3.5",
                          " * WC tested up to: 3.8.1"], new_lines)

    def test_get_updated_internal_file_lines_woocommerce_readme_txt_file(self):
        file_lines = ["Requires at least: 4.9",
                      "Tested up to: 5.2",
                      "Requires PHP: 5.6",
                      "Stable tag: 3.2.1"]
        shop_extension_file_list = FileActionHelper.get_data_from_internal_files()['woocommerce']
        replace_hint_entries = shop_extension_file_list["readme.txt"]
        new_lines = self.internal_file_updater_with_platform.get_updated_internal_file_lines(file_lines,
                                                                                             replace_hint_entries)
        self.assertEqual(["Requires at least: 5.0.3",
                          "Tested up to: 5.3",
                          "Requires PHP: 7.1",
                          "Stable tag: 3.2.2"], new_lines)

    def test_get_lines_with_replaced_php_badges(self):
        file_lines = ["[![PHP v5.6](https://img.shields.io/badge/php-v5.6-yellow.svg)](http://www.php.net)",
                      "[![PHP v7.0](https://img.shields.io/badge/php-v7.0-yellow.svg)](http://www.php.net)",
                      "[![PHP v7.1](https://img.shields.io/badge/php-v7.1-yellow.svg)](http://www.php.net)"]
        new_lines = self.internal_file_updater_with_platform.get_lines_with_replaced_php_badges(file_lines,
                                                                                                "http://www.php.net")
        self.assertEqual(["[![PHP v7.1](https://img.shields.io/badge/php-v7.1-yellow.svg)](http://www.php.net)",
                          "[![PHP v7.2](https://img.shields.io/badge/php-v7.2-yellow.svg)](http://www.php.net)"],
                         new_lines)

    def test_get_lines_with_replaced_badges_shopsystem(self):
        file_lines = ["[![WooCommerce v3.1.1](https://img.shields.io/badge/WooCommerce-v3.1.1-green.svg)](https://woocommerce.com/)",
                      "[![Wordpress v5.0.3](https://img.shields.io/badge/Wordpress-v5.0.3-green.svg)](https://wordpress.org/)"]
        new_lines = self.internal_file_updater_with_platform.get_lines_with_replaced_badges(
            file_lines, "https://woocommerce.com/", "shopsystem_compatible_highest_version")
        self.assertEqual(["[![WooCommerce v3.8.0](https://img.shields.io/badge/WooCommerce-v3.8.0-green.svg)](https://woocommerce.com/)",
                      "[![Wordpress v5.0.3](https://img.shields.io/badge/Wordpress-v5.0.3-green.svg)](https://wordpress.org/)"],
                         new_lines)

    def test_get_lines_with_replaced_badges_platform(self):
        file_lines = ["[![WooCommerce v3.8.0](https://img.shields.io/badge/WooCommerce-v3.8.0-green.svg)](https://woocommerce.com/)",
                      "[![Wordpress v5.0.3](https://img.shields.io/badge/Wordpress-v5.0.3-green.svg)](https://wordpress.org/)"]
        new_lines = self.internal_file_updater_with_platform.get_lines_with_replaced_badges(
            file_lines,"https://wordpress.org/", "platform_compatible_highest_version")
        self.assertEqual(["[![WooCommerce v3.8.0](https://img.shields.io/badge/WooCommerce-v3.8.0-green.svg)](https://woocommerce.com/)",
                      "[![Wordpress v5.3](https://img.shields.io/badge/Wordpress-v5.3-green.svg)](https://wordpress.org/)"],
                         new_lines)
