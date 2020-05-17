from src.FileActionHelper import FileActionHelper
from bs4 import element
import html2markdown
from src.Constants import Constants
from src.StringActionHelper import StringActionHelper
from src.FileUpdater import FileUpdater
import os


def get_first_sign_in_table_row_index(table_cells) -> int:
    """
    Returns index of the first special sign in a raw
    :return: int
    """
    signs_in_table = []
    for cell in table_cells:
        if (Constants.TICK_SIGN_IN_CHANGELOG in cell) \
                or (Constants.TICK_SIGN_IN_CHANGELOG_UNICODE in cell) \
                or (Constants.CROSS_SIGN_IN_CHANGELOG in cell):
            signs_in_table.append(cell)
    return table_cells.index(signs_in_table[0])


def get_new_table_row(cell_list, new_cell_index, new_cells):
    """
    Returns table raw with with new cells
    :return: string
    """
    new_table_row = cell_list[0: new_cell_index] + new_cells
    new_table_row.append(cell_list[len(cell_list) - 1])
    return Constants.TABLE_COLUMN_SPLITTER_IN_CHANGELOG.join(new_table_row)


class ChangelogFileUpdater(FileUpdater):

    def __init__(self,
                 extension,
                 release_candidate_version,
                 last_released_version,
                 php_compatibility_versions,
                 php_tested_versions,
                 shopsystem_compatibility_versions,
                 shopsystem_tested_versions,
                 platform_compatibility_versions=None,
                 platform_tested_versions=None):
        super().__init__(extension,
                         release_candidate_version,
                         last_released_version,
                         php_compatibility_versions,
                         php_tested_versions,
                         shopsystem_compatibility_versions,
                         shopsystem_tested_versions,
                         platform_compatibility_versions,
                         platform_tested_versions)

    def add_new_release_entry_to_changelog(self):
        """
        Adds new entry to changelog file
        """
        soup, changelog_data = FileActionHelper.get_changelog_markdown_entries(self.extension)
        header_entry = soup.new_tag(Constants.RELEASE_HEADER_TAG_IN_CHANGELOG)
        header_entry.string = self.release_candidate_version
        soup.h2.insert_before(header_entry)
        soup.h2.insert_after(element.NavigableString(Constants.NEW_LINE))
        table_entry = soup.new_tag(Constants.TABLE_TAG_IN_CHANGELOG)
        table_entry_contents = \
            FileActionHelper.get_changelog_markdown_entry_part(self.extension,
                                                               self.last_released_version, 'table').contents
        table_entry.contents = table_entry_contents
        self.update_table_rows(table_entry_contents)
        soup.h2.insert_after(table_entry)
        soup.p.insert_before(element.NavigableString(Constants.NEW_LINE))
        print("Updating CHANGELOG file")
        with open(FileActionHelper.get_file_path_by_config_key(self.extension, Constants.CHANGELOG_FILE), 'w') as f:
            f.write(html2markdown.convert(str(soup)))

    def update_table_rows(self, table_entry_contents):
        """
        Updates changelog table
        """
        for entry in table_entry_contents:
            if isinstance(entry, element.NavigableString):
                if Constants.OVERVIEW_IN_CHANGELOG in entry.string:
                    new_entry_text = self.get_compatible_php_versions_table_header_string(entry.string)
                    table_entry_contents[table_entry_contents.index(entry)].string.replace_with(new_entry_text)
                if ":|" in entry.string:
                    new_entry_text = self.get_row_separator_table_row(entry.string)
                    table_entry_contents[table_entry_contents.index(entry)].string.replace_with(new_entry_text)
            if isinstance(entry, element.Tag):
                if Constants.TESTED_IN_CHANGELOG in entry.text:
                    new_entry_text = self.get_tested_shopsystem_and_platform_versions_table_string(
                        entry.nextSibling.string)
                    new_entry_text = self.get_tested_php_versions_table_string(new_entry_text)
                    table_entry_contents[table_entry_contents.index(entry)].nextSibling.string.replace_with(
                        new_entry_text)
                if Constants.COMPATIBILITY_IN_CHANGELOG in entry.text:
                    new_entry_text = self.get_compatibility_shopsystem_and_platform_versions_table_string(
                        entry.nextSibling.string)
                    new_entry_text = self.get_compatible_php_versions_table_string(new_entry_text)
                    table_entry_contents[table_entry_contents.index(entry)].nextSibling.string.replace_with(
                        new_entry_text)

    def get_compatible_php_versions_table_header_string(self, table_row) -> str:
        """
        Returns header table entry row with php versions
        :return: string
        """
        table_cells = table_row.split(Constants.TABLE_COLUMN_SPLITTER_IN_CHANGELOG)
        first_php_index = FileUpdater.get_index_of_first_list_entry_containing_text(table_cells, Constants.PHP_IN_CHANGELOG)
        new_php_cells = []
        for version in self.php_compatibility_versions:
            new_php_cells.append(" {} {} ".format(Constants.PHP_IN_CHANGELOG, version))
        return get_new_table_row(table_cells, first_php_index, new_php_cells)

    def get_tested_php_versions_table_string(self, table_row) -> str:
        """
        Returns table entry row with tested php versions
        :return: string
        """
        table_cells = table_row.split(Constants.TABLE_COLUMN_SPLITTER_IN_CHANGELOG)
        intersection_list = list(set(self.php_compatibility_versions).intersection(self.php_tested_versions))
        tick_positions = []
        for intersection_version in intersection_list:
            tick_positions.append(self.php_compatibility_versions.index(intersection_version))
        new_sign_cells = self.get_new_sign_cells(tick_positions)
        return get_new_table_row(table_cells, get_first_sign_in_table_row_index(table_cells), new_sign_cells)

    def get_compatible_php_versions_table_string(self, table_row) -> str:
        """
        Returns table entry row with compatible php versions
        :return: string
        """
        table_cells = table_row.split(Constants.TABLE_COLUMN_SPLITTER_IN_CHANGELOG)
        tick_positions = [self.php_compatibility_versions.index(a) for a in self.php_compatibility_versions]
        new_sign_cells = self.get_new_sign_cells(tick_positions)
        return get_new_table_row(table_cells, get_first_sign_in_table_row_index(table_cells), new_sign_cells)

    def get_new_sign_cells(self, tick_positions) -> list:
        """
        Returns string with table entry row filled with crosses or ticks
        :return: string
        """
        new_sign_cells = []
        for version in self.php_compatibility_versions:
            sign_to_put = "   {}   ".format(Constants.CROSS_SIGN_IN_CHANGELOG)
            if self.php_compatibility_versions.index(version) in tick_positions:
                sign_to_put = " {} ".format(Constants.TICK_SIGN_IN_CHANGELOG_UNICODE)
            new_sign_cells.append("{}".format(sign_to_put))
        return new_sign_cells

    def get_tested_shopsystem_and_platform_versions_table_string(self, table_row):
        """
        Returns table entry row with tested shop system and platform versions
        :return: string
        """
        return self.get_shopsystem_and_platform_versions_table_string(table_row, self.shopsystem_tested_versions,
                                                                      self.platform_tested_versions)

    def get_compatibility_shopsystem_and_platform_versions_table_string(self, table_row):
        """
        Returns table entry row with compatible shop system and platform versions
        :return: string
        """
        return self.get_shopsystem_and_platform_versions_table_string(table_row, self.shopsystem_compatibility_versions,
                                                                      self.platform_compatibility_versions)

    def get_shopsystem_and_platform_versions_table_string(self, table_row, shopsystem_version_range,
                                                          platform_version_range) -> str:
        """
        Returns table entry row with updated shop system and platform versions
        :return: string
        """
        table_cells = table_row.split(Constants.TABLE_COLUMN_SPLITTER_IN_CHANGELOG)
        for cell in table_cells:
            if self.extension in cell.lower():
                index = table_cells.index(cell)
                versions = cell.split(',')
                versions[0] = versions[0].replace(StringActionHelper.find_part_to_replace(versions[0]),
                                                  ' - '.join(shopsystem_version_range))
                table_cells[index] = versions[0]
                if len(versions) > 1 and platform_version_range is not None:
                    versions[1] = versions[1].replace(StringActionHelper.find_part_to_replace(versions[1]),
                                                      ' - '.join(platform_version_range))
                    table_cells[index] = ",".join(versions)
        return Constants.TABLE_COLUMN_SPLITTER_IN_CHANGELOG.join(table_cells)

    def get_row_separator_table_row(self, table_row):
        """
        Returns table entry row with updated shop system and platform versions
        :return: string
        """
        table_cells = table_row.split(Constants.TABLE_COLUMN_SPLITTER_IN_CHANGELOG)
        first_special_cell_index = FileUpdater.get_index_of_first_list_entry_containing_text(table_cells, ":")
        new_special_cells = [Constants.ROW_SEPARATOR_IN_CHANGELOG for i in self.php_compatibility_versions]
        return get_new_table_row(table_cells, first_special_cell_index, new_special_cells)

    # @staticmethod
    # def get_index_of_first_cell_containing_text(cell_list, text) -> int:
    #     """
    #     Returns index of first cell from containing text from cell list
    #     :return: int
    #     """
    #     cells_containing_text = [s for s in cell_list if text in s]
    #     return cell_list.index(cells_containing_text[0])

# changelog = ChangelogUpdater('woocommerce', 'v3.2.2', 'v3.2.1', ['7.1', '7.2'],
#                              ['7.2'], ['3.3.6', '3.9.0'], ['3.8.0'], ['1.1.1'], ['1.1.1', '2.2.2'])
# changelog.add_new_release_entry_to_changelog()
