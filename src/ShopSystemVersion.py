from src.FileActionHelper import FileActionHelper
from src.Constants import Constants
from bs4 import element
import re


class ShopSystemVersion:

    def __init__(self, extension, last_released_version):
        self.extension = extension
        self.last_released_version = last_released_version
        self.compatible_shopsystem_versions_range = []
        self.compatible_platform_versions_range = []
        self.tested_shopsystem_versions_from_config_range = []
        self.tested_shopsystem_versions_from_changelog_range = []
        self.tested_platform_versions_range = []
        self.set_compatible_versions_from_config()
        self.set_tested_platform_versions()
        self.set_tested_shopsystem_versions_from_config()

    def set_compatible_versions_from_config(self):
        """
         Sets compatible shop systems and platform ranges from changelog latest entry
         """
        compatible_versions_ranges = self.get_version_ranges(Constants.COMPATIBILITY_IN_CHANGELOG)
        self.compatible_shopsystem_versions_range = compatible_versions_ranges[0].split('-')
        if len(compatible_versions_ranges) > 1:
            self.compatible_platform_versions_range = compatible_versions_ranges[1].split('-')

    def set_tested_platform_versions(self):
        """
         Sets tested platform ranges from changelog latest entry
         """
        tested_versions_ranges = self.get_version_ranges(Constants.TESTED_IN_CHANGELOG)
        if len(tested_versions_ranges) > 1:
            self.tested_platform_versions_range = tested_versions_ranges[1].split('-')

    def set_tested_shopsystem_versions_from_config(self):
        """
         Sets tested shop systems from config
         """
        self.tested_shopsystem_versions_from_config_range = FileActionHelper.get_data_from_compatible_shop_releases_text_file(self.extension)

    def get_version_ranges(self, version_type):
        """
        Returns range of requested versions
        :return: list
        """
        last_release_compatibility_table = \
            FileActionHelper.get_changelog_markdown_entry_part(self.extension, self.last_released_version, 'table')
        versions_ranges = self.get_versions_from_table(
            last_release_compatibility_table, version_type)
        return versions_ranges

    @staticmethod
    def get_versions_from_table(compatibility_table, version_type) -> list:
        """
        Returns range of compatibility versions from BeautifulSoup format table
        :return: list
        """
        compatibility_string = ''
        for line in compatibility_table.contents:
            if isinstance(line, element.Tag) and version_type in line.text:
                compatibility_string = str(line.next_sibling)
        compatibility_list = compatibility_string.split(',')
        compatibility_ranges = []
        for entry in compatibility_list:
            compatibility_version_range = re.sub('[^\d\.-]', '', entry)
            compatibility_ranges.append(compatibility_version_range)
        return compatibility_ranges

    def get_compatible_shopsystem_versions_range(self) -> list:
        """
        Returns range of shop system compatibility versions
        :return: list
        """
        return self.compatible_shopsystem_versions_range

    def get_compatible_platform_versions_range(self) -> list:
        """
        Returns range of platform compatibility versions
        :return: list
        """
        return self.compatible_platform_versions_range

    def get_tested_shopsystem_versions_range_from_config(self) -> list:
        """
        Returns range of shop system tested versions from config
        :return: list
        """
        return self.tested_shopsystem_versions_from_config_range

    def get_tested_platform_versions_range(self) -> list:
        """
        Returns range of platform tested versions from changelog
        :return: list
        """
        return self.tested_platform_versions_range

    def set_tested_shopsystem_versions_range_from_changelog(self):
        tested_versions_ranges = self.get_version_ranges(Constants.TESTED_IN_CHANGELOG)
        self.tested_shopsystem_versions_from_changelog_range = tested_versions_ranges[0].split('-')

    def get_tested_shopsystem_versions_range_from_changelog(self) -> list:
        """
        Returns range of shopsystem tested versions from changelog
        :return: list
        """
        self.set_tested_shopsystem_versions_range_from_changelog()
        return self.tested_shopsystem_versions_from_changelog_range
