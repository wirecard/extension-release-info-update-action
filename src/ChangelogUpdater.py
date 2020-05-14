from src.FileActionHelper import FileActionHelper
import copy
from bs4 import NavigableString
from src.Constants import Constants

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
        soup.h2.insert_after(NavigableString(Constants.NEW_LINE))
        table_entry = soup.new_tag(Constants.TABLE_TAG_IN_CHANGELOG)
        table_entry_text = FileActionHelper.get_changelog_markdown_entry_part(self.extension, self.last_released_version, 'table').text
        table_entry.string = table_entry_text
        soup.h2.insert_after(table_entry)
        soup.p.insert_before(NavigableString(Constants.NEW_LINE))
        #modify text
        print(soup)


changelog = ChangelogUpdater('woocommerce', 'v3.2.2', '3.2.1', ['7.1', '7.2'],
                             ['7.2'], ['3.3.4', '3.8.0'], ['3.8.0'])
changelog.add_new_release_entry_to_changelog()
