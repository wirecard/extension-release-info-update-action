from src.Constants import Constants
from termcolor import colored, cprint
import sys


class FileUpdater:

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

    @staticmethod
    def get_index_of_first_list_entry_containing_text(entry_list, text) -> int:
        """
        Returns index of first element from containing text from list
        :return: int
        """
        cells_containing_text = [s for s in entry_list if text in s]
        try:
            return entry_list.index(cells_containing_text[0])
        except IndexError:
            cprint(colored("{} Line containing string '{}' does not exist in the file. Please update {} {}".
                           format(Constants.PRETTY_LOG_ADDITION,
                                  text,
                                  Constants.SHOP_EXTENSION_INTERNAL_FILES_JSON_FILE_PATH,
                                  Constants.PRETTY_LOG_ADDITION)), 'red', attrs=['bold'], file=sys.stderr)
