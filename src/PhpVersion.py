from src.FileActionHelper import FileActionHelper
from src.Constants import Constants
from src.StringActionHelper import StringActionHelper
from src.ChangelogTableHelper import ChangelogTableHelper
from bs4 import element


class PhpVersion:

    def __init__(self, extension, release_version=''):
        self.extension = extension
        self.release_version = release_version
        self.compatible_php_versions_from_config = []
        self.tested_php_versions_from_config = []
        self.tested_php_versions_from_changelog = []
        self.compatible_php_versions_from_changelog = []
        self.set_compatible_php_version_from_config()
        self.set_tested_php_versions_from_config()

    def set_tested_php_versions_from_config(self):
        """
        Sets tested php versions from ui test settings
        """
        workflow_data = FileActionHelper.get_data_from_workflow_file(self.extension,
                                                                     Constants.UI_TEST_WORKFLOW)
        tested_php_versions = workflow_data['jobs']['include'][0]['php']
        if isinstance(tested_php_versions, list):
            for version in tested_php_versions:
                self.tested_php_versions_from_config.append(str(version))
        if isinstance(tested_php_versions, float):
            self.tested_php_versions_from_config = [str(tested_php_versions)]

    def set_compatible_php_version_from_config(self):
        """
        Sets tested php versions from unit test settings
        """
        workflow_data = FileActionHelper.get_data_from_workflow_file(self.extension,
                                                                     Constants.UNIT_TEST_WORKFLOW)
        self.compatible_php_versions_from_config = workflow_data['jobs']['run']['strategy']['matrix']['php-versions']

    def get_compatible_php_versions_from_config(self) -> list:
        """
        Returns compatible php versions from config
        :return: list
        """
        return self.compatible_php_versions_from_config

    def get_tested_php_versions_from_config(self) -> list:
        """
        Returns tested php versions from config
        :return: list
        """
        return self.tested_php_versions_from_config

    def set_tested_php_versions_from_changelog(self):
        """
        Sets tested php versions from changelog entry
        """
        self.set_compatible_php_versions_from_changelog()
        changelog_table = FileActionHelper.get_changelog_markdown_entry_part(self.extension,
                                                                             self.release_version, 'table')

        table_cells = ChangelogTableHelper.get_php_version_list_from_table(changelog_table, "tested")
        tick_positions = []
        table_part_with_signs = table_cells[ChangelogTableHelper.get_first_sign_in_table_row_index(table_cells):]
        for cell in table_part_with_signs:
            if ChangelogTableHelper.is_tick_in_string(cell):
                tick_positions.append(table_part_with_signs.index(cell))
        for pos in tick_positions:
            self.tested_php_versions_from_changelog.append(self.compatible_php_versions_from_changelog[pos])

    def set_compatible_php_versions_from_changelog(self):
        """
        Sets compatible php versions from changelog entry
        """
        changelog_table = FileActionHelper.get_changelog_markdown_entry_part(self.extension,
                                                                             self.release_version, 'table')
        table_cells = ChangelogTableHelper.get_php_version_list_from_table(changelog_table, "compatibility")
        for cell in table_cells:
            if Constants.PHP_IN_CHANGELOG in cell:
                self.compatible_php_versions_from_changelog.append(StringActionHelper.find_part_to_replace(cell))

    def get_tested_php_versions_from_changelog(self):
        """
        Returns tested php versions from changelog
        :return: list
        """
        self.set_tested_php_versions_from_changelog()
        return self.tested_php_versions_from_changelog

    def get_compatible_php_versions_from_changelog(self):
        """
        Returns compatible php versions from changelog
        :return: list
        """
        self.set_compatible_php_versions_from_changelog()
        return self.compatible_php_versions_from_changelog

