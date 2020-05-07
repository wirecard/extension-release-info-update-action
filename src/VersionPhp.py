import json
import re
import git
from src.FileFinder import FileFinder
import yaml


class VersionPhp:

    def __init__(self, extension, config_files_json_file_name):
        self.config_files_json = config_files_json_file_name
        self.extension = extension
        self.compatible_php_versions = []
        self.tested_php_versions = []
        self.set_compatible_php_versions()

    # @staticmethod
    # def set_compatible_php_versions(self):
    #     """
    #     Sets compatible php versions from php unit workflow
    #     """
    #     self.compatible_php_versions = self.find_compatible_php_versions()

    def set_tested_php_versions(self):
        """
        Sets current release version from branch name
        """
        pass
        # repo = git.Repo(search_parent_directories=True)
        # branch = repo.active_branch
        # self.version = re.sub('[^\d\.]', '', branch.name)

    def set_compatible_php_versions(self):
        yaml_full_path = FileFinder.get_file_path(self.get_unit_test_pipeline_file_name())
        with open(yaml_full_path) as yaml_file:
            yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
            self.compatible_php_versions = yaml_data['jobs']['run']['strategy']['matrix']['php-versions']

    def get_unit_test_pipeline_file_name(self):
        with open(self.config_files_json) as handle:
            test = json.loads(handle.read())
            print(test)
            unit_test_pipeline_file = test[self.extension]['unit_test_pipeline']
        print("Unit test pipeline file name :" + unit_test_pipeline_file)
        return unit_test_pipeline_file

    def get_compatible_php_versions(self):
        return self.compatible_php_versions

# test = VersionPhp('woocommerce', 'shop-extensions-config-files.json')
