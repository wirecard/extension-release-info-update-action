from src.FileActionHelper import FileActionHelper
from src.Constants import Constants


class PhpVersion:

    def __init__(self, extension):
        self.extension = extension
        self.compatible_php_versions_from_config = []
        self.tested_php_versions_from_config = []
        self.tested_php_versions_from_changelog = []
        self.compatible_php_versions_from_changelog = []
        self.set_compatible_php_version_from_config()
        self.set_tested_php_versions_from_config()

    def set_tested_php_versions_from_config(self):
        """
        Sets tested php versions from ui test settings
        """
        workflow_data = FileActionHelper.get_data_from_workflow_file(self.extension,
                                                                     Constants.UI_TEST_WORKFLOW)
        tested_php_versions = workflow_data['jobs']['include'][0]['php']
        if isinstance(tested_php_versions, list):
            for version in tested_php_versions:
                self.tested_php_versions_from_config.append(str(version))
        if isinstance(tested_php_versions, float):
            self.tested_php_versions_from_config = [str(tested_php_versions)]

    def set_compatible_php_version_from_config(self):
        """
        Sets tested php versions from unit test settings
        """
        workflow_data = FileActionHelper.get_data_from_workflow_file(self.extension,
                                                                     Constants.UNIT_TEST_WORKFLOW)
        self.compatible_php_versions_from_config = workflow_data['jobs']['run']['strategy']['matrix']['php-versions']

    def get_compatible_php_versions_from_config(self) -> list:
        """
        Returns compatible php versions from config
        :return: list
        """
        return self.compatible_php_versions_from_config

    def get_tested_php_versions_from_config(self) -> list:
        """
        Returns tested php versions from config
        :return: list
        """
        return self.tested_php_versions_from_config

    def set_tested_php_versions_from_changelog(self):
        pass

    def set_compatible_php_versions_from_changelog(self):
        pass

    def get_tested_php_versions_from_changelog(self):
        """
        Returns tested php versions from changelog
        :return: list
        """
        return self.tested_php_versions_from_changelog

    def get_compatible_php_versions_from_changelog(self):
        """
        Returns compatible php versions from changelog
        :return: list
        """
        return self.compatible_php_versions_from_changelog
