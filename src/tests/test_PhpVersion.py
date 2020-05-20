from unittest import TestCase
from src.PhpVersion import PhpVersion


class TestPhpVersion(TestCase):

    def setUp(self) -> None:
        self.phpVersion = PhpVersion('woocommerce', 'v3.2.1')

    def test_get_tested_php_versions(self):
        self.assertEquals(self.phpVersion.get_tested_php_versions_from_config(), ['7.2'])

    def test_get_compatible_php_versions(self):
        self.assertEquals(self.phpVersion.get_compatible_php_versions_from_config(), ['5.6', '7.0', '7.1', '7.2'])

    def test_get_compatible_php_versions_from_changelog(self):
        self.assertEquals(self.phpVersion.get_compatible_php_versions_from_changelog(), ['5.6', '7.0', '7.1', '7.2'])

    def test_set_tested_php_versions_from_changelog(self):
        self.assertEquals(self.phpVersion.get_tested_php_versions_from_changelog(), ['7.2'])
