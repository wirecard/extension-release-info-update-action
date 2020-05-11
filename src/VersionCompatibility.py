from src.FileActionHelper import FileActionHelper
from src.Constants import Constants
from bs4 import BeautifulSoup
import re


class VersionCompatibility:

    def __init__(self, extension, last_released_version):
        self.extension = extension
        self.last_released_version = last_released_version
        self.compatible_shopsystem_versions_range = []
        self.compatible_platform_versions_range = []
        self.tested_shopsystem_versions_range = []
        self.tested_platform_versions_range = []
        self.set_compatible_versions()
        self.set_tested_versions()

    def set_compatible_versions(self):
        """
         Sets current release candidate compatible shop systems range
         """
        compatible_versions_ranges = self.get_version_ranges(Constants.COMPATIBILITY_IN_CHANGELOG)
        self.compatible_shopsystem_versions_range = compatible_versions_ranges[0].split('-')
        if len(compatible_versions_ranges) > 1:
            self.compatible_platform_versions_range = compatible_versions_ranges[1].split('-')

    def set_tested_versions(self):
        """
         Sets current release candidate tested shop systems range
         """
        tested_versions_ranges = self.get_version_ranges(Constants.TESTED_IN_CHANGELOG)
        self.tested_shopsystem_versions_range = tested_versions_ranges[0].split('-')
        if len(tested_versions_ranges) > 1:
            self.tested_platform_versions_range = tested_versions_ranges[1].split('-')

    def get_version_ranges(self, version_type):
        """
        Returns range of requested versions
        :return: list
        """
        last_release_compatibility_table = self.get_last_release_compatibility_table()
        versions_ranges = self.get_versions_from_table(
            last_release_compatibility_table, version_type)
        return versions_ranges

    def get_last_release_compatibility_table(self):
        """
        Returns bs4 format table from changelog markdown
        :return: BeautifulSoup tag
        """
        changelog_data = FileActionHelper.get_data_from_markdown_file(self.extension, Constants.CHANGELOG_FILE)
        soup = BeautifulSoup(changelog_data, 'html.parser')
        extension_releases = soup.find_all('h2')
        position = 0
        for entry in extension_releases:
            if self.last_released_version in entry:
                position = extension_releases.index(entry)
        return soup.find_all('p')[position]

    @staticmethod
    def get_versions_from_table(compatibility_table, version_type) -> list:
        """
        Returns range of compatibility versions from BeautifulSoup format table
        :return: list
        """
        compatibility_string = ''
        for line in compatibility_table.contents:
            if "Tag" in str(type(line)) and version_type in line.text:
                compatibility_string = str(line.next_sibling)
        compatibility_array = compatibility_string.split(',')
        compatibility_ranges = []
        for entry in compatibility_array:
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

    def get_tested_shopsystem_versions_range(self) -> list:
        """
        Returns range of shop system tested versions
        :return: list
        """
        return self.tested_shopsystem_versions_range

    def get_tested_platform_versions_range(self) -> list:
        """
        Returns range of platform tested versions
        :return: list
        """
        return self.tested_platform_versions_range

