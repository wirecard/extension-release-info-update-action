from src.FileActionHelper import FileActionHelper
import copy
from bs4 import element
import markdown
from src.Constants import Constants
import html2markdown
from src.Constants import Constants


class ChangelogUpdater:

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
        self.extension = extension
        self.release_candidate_version = release_candidate_version
        self.last_released_version = last_released_version
        self.php_compatibility_versions = php_compatibility_versions
        self.php_tested_versions = php_tested_versions
        self.shopsystem_compatibility_versions = shopsystem_compatibility_versions
        self.shopsystem_tested_versions = shopsystem_tested_versions
        self.platform_compatibility_versions = platform_compatibility_versions
        self.platform_tested_versions = platform_tested_versions

    def add_new_release_entry_to_changelog(self):
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
        self.update_versions(table_entry_contents)
        soup.h2.insert_after(table_entry)
        soup.p.insert_before(element.NavigableString(Constants.NEW_LINE))
        with open('test.md', 'w') as f:
            f.write(html2markdown.convert(str(soup)))

    def update_versions(self, table_entry_contents):
        for entry in table_entry_contents:
            if isinstance(entry, element.NavigableString):
                if Constants.OVERVIEW_IN_CHANGELOG in entry.string:
                    print(entry)
                    self.update_compatible_php_versions(entry)
                if Constants.TESTED_IN_CHANGELOG:
                    self.update_tested_php_versions()
                    self.update_tested_shopsystem_versions()
                    self.update_tested_platform_versions()
                if Constants.COMPATIBILITY_IN_CHANGELOG:
                    self.update_compatible_shopsystem_versions()
                    self.update_compatible_platform_versions()

    def update_compatible_php_versions(self, entry):
        pass

    def update_tested_php_versions(self):
        pass

    def update_tested_shopsystem_versions(self):
        pass

    def update_tested_platform_versions(self):
        pass

    def update_compatible_shopsystem_versions(self):
        pass

    def update_compatible_platform_versions(self):
        pass


changelog = ChangelogUpdater('woocommerce', 'v3.2.2', '3.2.1', ['7.1', '7.2'],
                             ['7.2'], ['3.3.4', '3.8.0'], ['3.8.0'])
changelog.add_new_release_entry_to_changelog()
