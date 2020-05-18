from unittest import TestCase
from src.FileUpdater import FileUpdater


class TestFileUpdater(TestCase):

    def test_get_index_of_first_list_entry_containing_text(self):
        file_lines = ["abc_123", "sdf"]
        index = FileUpdater.get_index_of_first_list_entry_containing_text(file_lines, "abc")
        self.assertEqual(0, index)

