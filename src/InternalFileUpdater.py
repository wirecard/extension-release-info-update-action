from src.FileActionHelper import FileActionHelper


class InternalFileUpdater:

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
        self.internal_files_entry_to_output_info_dict = {
            "extension_version": self.release_candidate_version,
            "shopsystem_tested_highest_version": sorted(self.shopsystem_tested_versions[-1]),
            "shopsystem_lowest_compatible_version": sorted(self.shopsystem_compatibility_versions[0]),
            "php_lowest_version": sorted(self.php_compatibility_versions[0]),
            "platform_version_lowest_compatible_version": sorted(self.platform_compatibility_versions[0]),
        }

    def update_internal_files(self):
        shop_extension_file_list = FileActionHelper.get_data_from_internal_files()[self.extension]
        print(shop_extension_file_list)
        for file_name, file_entries in shop_extension_file_list.items():
            with open(file_name, 'w') as internal_file:
                file_lines = internal_file.readlines()
                for hint in file_entries.value():
                    replace_line_index = self.get_file_line_containing_hint_index(file_lines, hint)
                    file_lines[replace_line_index] = file_lines[replace_line_index].replace(
                        self.get_replaceble_string(), self.internal_files_entry_to_output_info_dict[hint])

    def get_file_line_containing_hint_index(self, file_lines, hint):
        for line in file_lines:
            if hint in line:
                return file_lines[line].index
            return None

    def get_replaceble_string(self):
        return ""


updater = InternalFileUpdater('woocommerce', 'v3.2.2', 'v3.2.1', ['7.1', '7.2'],
                              ['7.2'], ['3.3.6', '3.9.0'], ['3.8.0'], ['1.1.1'], ['1.1.1', '2.2.2'])
updater.update_internal_files()
