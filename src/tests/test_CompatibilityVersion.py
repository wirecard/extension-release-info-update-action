from unittest import TestCase
from src.CompatibilityVersion import CompatibilityVersion


class TestCompatibilityVersion(TestCase):

    def setUp(self) -> None:
        self.compatibilityVersion = CompatibilityVersion('woocommerce',  'v3.2.1')

    def test_get_compatible_shopsystem_versions_range(self):
        self.assertEqual(self.compatibilityVersion.get_compatible_shopsystem_versions_range(), ['3.3.4', '3.8.0'])

    def test_get_compatible_platform_versions_range(self):
        self.assertEqual(self.compatibilityVersion.get_compatible_platform_versions_range(), ['5.0.3', '5.3'])

    def test_get_tested_shopsystem_versions_range(self):
        self.assertEqual(self.compatibilityVersion.get_tested_shopsystem_versions_range(), ['3.8.0'])

    def test_get_tested_platform_versions_range(self):
        self.assertEqual(self.compatibilityVersion.get_tested_platform_versions_range(), ['5.3'])
