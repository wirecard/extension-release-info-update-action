from unittest import TestCase
from src.FileUpdater import FileUpdater


class TestFileUpdater(TestCase):

    def test_get_index_of_first_list_entry_containing_text(self):
        file_lines = ["abc_123", "sdf"]
        index = FileUpdater.get_index_of_first_list_entry_containing_text(file_lines, "abc")
        self.assertEqual(0, index)


    # def test_get_index_of_last_list_entry_containing_text(self):
    #     file_lines = ["abc_123", "sdf", "abc_123"]
    #     index = FileUpdater.get_index_of_last_list_entry_containing_text(file_lines, "abc")
    #     self.assertEqual(2, index)
