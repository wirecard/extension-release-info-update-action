from src.FileActionHelper import FileActionHelper
from src.Constants import Constants


class ChangelogUpdater:

    def __init__(self,
                 extension,
                 release_candidate_version,
                 php_compatibility_versions,
                 php_tested_versions,
                 shopsystem_compatibility_versions,
                 shopsystem_tested_versions,
                 platform_compatibility_versions=None,
                 platform_tested_versions=None):
        self.extension = extension
        self.release_candidate_version = release_candidate_version
        self.php_compatibility_versions = php_compatibility_versions
        self.php_tested_versions = php_tested_versions
        self.shopsystem_compatibility_versions = shopsystem_compatibility_versions
        self.shopsystem_tested_versions = shopsystem_tested_versions
        self.platform_compatibility_versions = platform_compatibility_versions
        self.platform_tested_versions = platform_tested_versions

    def add_new_release_entry_to_changelog(self):
        soup, changelog_data = FileActionHelper.get_changelog_markdown_entries(self.extension)
        intermediate_entry = changelog_data[0]
        intermediate_entry['text'] = self.release_candidate_version
        changelog_data.insert(0, intermediate_entry)
        print(soup, changelog_data)


changelog = ChangelogUpdater('woocommerce', 'v3.2.2', ['7.1', '7.2'],
                             ['7.2'], ['3.3.4', '3.8.0'], ['3.8.0'])
changelog.add_new_release_entry_to_changelog()
