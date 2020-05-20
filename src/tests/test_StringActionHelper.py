from unittest import TestCase
from src.StringActionHelper import StringActionHelper


class TestStringActionHelper(TestCase):

    def test_find_part_to_replace_single_version(self):
        self.assertEqual("1.1.1", StringActionHelper.find_part_to_replace("Woocommerce 1.1.1"))

    def test_find_part_to_replace_version_range(self):
        self.assertEqual("1.1.1 - 2.2.2", StringActionHelper.find_part_to_replace("Woocommerce 1.1.1 - 2.2.2"))
