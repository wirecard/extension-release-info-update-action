from unittest import TestCase
from src.PhpVersion import PhpVersion


class TestPhpVersion(TestCase):

    def setUp(self) -> None:
        self.phpVersion = PhpVersion('woocommerce')

    def test_get_tested_php_versions(self):
        self.assertEquals(self.phpVersion.get_tested_php_versions(), 7.2)

    def test_get_compatible_php_versions(self):
        self.assertEquals(self.phpVersion.get_compatible_php_versions(), ['5.6', '7.0', '7.1', '7.2'])
