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
        self.set_tested_shopsystem_versions()

    def set_compatible_versions(self):
        """
         Sets current release candidate compatible shop systems range
         """
        last_release_compatibility_table = self.get_last_release_compatibility_table()
        compatible_versions_ranges = self.get_compatibility_versions_from_table(
            last_release_compatibility_table)
        self.compatible_shopsystem_versions_range = compatible_versions_ranges[0].split('-')
        if len(compatible_versions_ranges) > 1:
            self.compatible_platform_versions_range = compatible_versions_ranges[1].split('-')
        print(self.compatible_shopsystem_versions_range)

    def set_tested_shopsystem_versions(self):
        pass

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
    def get_compatibility_versions_from_table(compatibility_table) -> list:
        """
        Returns range of compatibility versions from BeautifulSoup format table
        :return: list
        """
        compatibility_string = ''
        for line in compatibility_table.contents:
            if "Tag" in str(type(line)) and "Compatibility" in line.text:
                compatibility_string = str(line.next_sibling)
        compatibility_array = compatibility_string.split(',')
        compatibility_ranges = []
        for entry in compatibility_array:
            compatibility_version_range = re.sub('[^\d\.-]', '', entry)
            compatibility_ranges.append(compatibility_version_range)
        return compatibility_ranges

version = VersionCompatibility('woocommerce', 'v3.2.1')
