from src.FileActionHelper import FileActionHelper
from src.Constants import Constants


class PhpVersion:

    def __init__(self, extension):
        self.extension = extension
        self.compatible_php_versions = []
        self.tested_php_versions = []
        self.set_compatible_php_versions()
        self.set_tested_php_versions()

    def set_tested_php_versions(self):
        """
        Sets tested php versions from ui test settings
        """
        workflow_data = FileActionHelper.get_data_from_workflow_file(self.extension,
                                                                     Constants.UI_TEST_WORKFLOW)
        tested_php_versions = workflow_data['jobs']['include'][0]['php']
        if isinstance(tested_php_versions, list):
            for version in tested_php_versions:
                self.tested_php_versions.append(str(version))
        if isinstance(tested_php_versions, float):
            self.tested_php_versions = [str(tested_php_versions)]

    def set_compatible_php_versions(self):
        """
        Sets tested php versions from unit test settings
        """
        workflow_data = FileActionHelper.get_data_from_workflow_file(self.extension,
                                                                     Constants.UNIT_TEST_WORKFLOW)
        self.compatible_php_versions = workflow_data['jobs']['run']['strategy']['matrix']['php-versions']

    def get_compatible_php_versions(self) -> list:
        """
        Returns compatible php versions
        :return: str
        """
        return self.compatible_php_versions

    def get_tested_php_versions(self) -> list:
        """
        Returns tested php versions
        :return: str
        """
        return self.tested_php_versions
