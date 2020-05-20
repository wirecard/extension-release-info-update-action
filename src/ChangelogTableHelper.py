from src.Constants import Constants
from bs4 import element


class ChangelogTableHelper:
    @staticmethod
    def get_php_version_list_from_table(changelog_table, version_type) -> list:
        """
        Return list of requested php versions from provided table
        :return: list
        """
        table_cells = []
        for entry in changelog_table:
            if isinstance(entry, element.NavigableString):
                if Constants.OVERVIEW_IN_CHANGELOG in entry.string and "compatibility" in version_type:
                    table_cells = entry.string.split(Constants.TABLE_COLUMN_SPLITTER_IN_CHANGELOG)
            if isinstance(entry, element.Tag):
                if Constants.TESTED_IN_CHANGELOG in entry.text and "tested" in version_type:
                    table_cells = entry.nextSibling.string.split(Constants.TABLE_COLUMN_SPLITTER_IN_CHANGELOG)
        return table_cells

    @staticmethod
    def get_first_sign_in_table_row_index(table_cells) -> int:
        """
        Returns index of the first special sign in a raw
        :return: int
        """
        signs_in_table = []
        for cell in table_cells:
            if ChangelogTableHelper.is_tick_in_string(cell) \
                    or (Constants.CROSS_SIGN_IN_CHANGELOG in cell):
                signs_in_table.append(cell)
        return table_cells.index(signs_in_table[0])

    @staticmethod
    def is_tick_in_string(string) -> bool:
        """
        Returns true if tick sign is in provided string
        :return: bool
        """
        return (Constants.TICK_SIGN_IN_CHANGELOG in string) or (Constants.TICK_SIGN_IN_CHANGELOG_UNICODE in string)
