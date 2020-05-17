from src.FileActionHelper import FileActionHelper
from src.StringActionHelper import StringActionHelper
from src.Constants import Constants
from src.FileUpdater import FileUpdater
import re


class InternalFileUpdater(FileUpdater):

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
        self.internal_files_entry_to_output_info_dict = {}
        self.set_internal_files_entry_to_output_info_dict()

    def set_internal_files_entry_to_output_info_dict(self):
        self.internal_files_entry_to_output_info_dict["extension_version"] = self.release_candidate_version
        self.internal_files_entry_to_output_info_dict["shopsystem_tested_highest_version"] = \
            (sorted(self.shopsystem_tested_versions)[-1] if len(
                self.shopsystem_tested_versions) > 1 else self.shopsystem_tested_versions[0])
        self.internal_files_entry_to_output_info_dict["shopsystem_compatible_lowest_version"] = \
            (sorted(self.shopsystem_compatibility_versions)[0] if len(
                self.shopsystem_compatibility_versions) > 1 else self.shopsystem_compatibility_versions[0])
        self.internal_files_entry_to_output_info_dict["shopsystem_compatible_highest_version"] = \
            (sorted(self.shopsystem_compatibility_versions)[-1] if len(
                self.shopsystem_compatibility_versions) > 1 else self.shopsystem_compatibility_versions[0])
        self.internal_files_entry_to_output_info_dict["php_compatible_lowest_version"] = \
            (sorted(self.php_compatibility_versions)[0] if len(
                self.php_compatibility_versions) > 1 else self.php_compatibility_versions[0])
        if self.platform_compatibility_versions:
            self.internal_files_entry_to_output_info_dict["platform_compatible_lowest_version"] = \
                (sorted(self.platform_compatibility_versions)[0] if len(
                    self.platform_compatibility_versions) > 1 else self.platform_compatibility_versions[0])
            self.internal_files_entry_to_output_info_dict["platform_compatible_highest_version"] = \
                (sorted(self.platform_compatibility_versions)[-1] if len(
                    self.platform_compatibility_versions) > 1 else self.platform_compatibility_versions[0])

    def update_files(self):
        """
        Updates all internal files from the internal-files.json
        """
        shop_extension_file_list = FileActionHelper.get_data_from_internal_files()[self.extension]
        for file_name, replace_hint_entries in shop_extension_file_list.items():
            print("Updating {}".format(file_name))
            file_lines = self.get_updated_file_lines(file_name, replace_hint_entries)
            with open(FileActionHelper.get_file_path(file_name), 'w') as internal_file:
                internal_file.writelines(file_lines)

    def get_updated_file_lines(self, file_name, replace_hint_entries) -> list:
        """
        Returns updated file lines for file
        :return: list
        """
        with open(FileActionHelper.get_file_path(file_name), 'r') as internal_file:
            file_lines = internal_file.readlines()
            if Constants.README_FILE in file_name:
                file_lines = self.get_updated_readme_badges(file_lines, replace_hint_entries)
            else:
                file_lines = self.get_updated_internal_file_lines(file_lines, replace_hint_entries)
        return file_lines

    def get_updated_internal_file_lines(self, file_lines, hint_entries) -> list:
        """
        Returns updated file lines for internal file
        :return: list
        """
        new_file_lines = file_lines
        for replace_field, hint in hint_entries.items():
            if Constants.INTERNAL_CHANGELOG_ENTRY_NAME in hint:
                new_file_lines = self.get_new_internal_changelog_entry(new_file_lines)
            else:
                replace_line_index = FileUpdater.get_index_of_first_list_entry_containing_text(new_file_lines, hint)
                value_to_replace = StringActionHelper.find_part_to_replace(new_file_lines[replace_line_index])
                new_value = self.internal_files_entry_to_output_info_dict[replace_field]
                new_file_lines[replace_line_index] = new_file_lines[replace_line_index].replace(
                    value_to_replace, new_value)
        return new_file_lines

    def get_new_internal_changelog_entry(self, file_lines):
        # TODO this should be called when CHANGELOG file is updated. Then we would have changelog comments
        # after string "== Changelog ==" add new release version and changelog commments
        return file_lines

    def get_updated_readme_badges(self, file_lines, hint_entries) -> list:
        """
        Returns file lines with updated readme badges
        :return: list
        """
        new_file_lines = file_lines
        for replace_field, hint in hint_entries.items():
            if Constants.PHP_IN_README_ENTRY_NAME in replace_field:
                new_file_lines = self.get_lines_with_replaced_php_badges(file_lines, hint)
            else:
                new_file_lines = self.get_lines_with_replaced_badges(new_file_lines, hint, replace_field)
        return new_file_lines

    def get_lines_with_replaced_php_badges(self, file_lines, hint) -> list:
        """
        Returns file lines updated php readme badges
        :return: list
        """
        php_index = FileUpdater.get_index_of_first_list_entry_containing_text(file_lines, hint)
        php_sample_line = file_lines[php_index]
        file_lines_without_php_badges = [x for x in file_lines if hint not in x]
        new_file_lines = file_lines_without_php_badges
        for php_version in reversed(self.php_compatibility_versions):
            new_file_lines.insert(php_index, re.sub('\d.\d', php_version, php_sample_line))
        return new_file_lines

    def get_lines_with_replaced_badges(self, file_lines, hint, replace_hint) -> list:
        """
        Returns file lines with updated badges (except php)
        :return: list
        """
        replace_index = FileUpdater.get_index_of_first_list_entry_containing_text(file_lines, hint)
        new_line = self.internal_files_entry_to_output_info_dict[replace_hint]
        substitute = re.search('\d\.\d\.\d', file_lines[replace_index])
        if substitute:
            file_lines[replace_index] = re.sub('\d\.\d\.\d', new_line, file_lines[replace_index])
        else:
            file_lines[replace_index] = re.sub('\d\.\d', new_line, file_lines[replace_index])
        return file_lines

