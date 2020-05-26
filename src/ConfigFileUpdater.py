from src.FileActionHelper import FileActionHelper
from src.StringActionHelper import StringActionHelper
from src.Constants import Constants
from src.FileUpdater import FileUpdater


class ConfigFileUpdater(FileUpdater):

    def __init__(self, extension,
                 php_compatibility_versions,
                 php_tested_versions,
                 shopsystem_tested_versions):
        super().__init__(extension,
                         None,
                         None,
                         php_compatibility_versions,
                         php_tested_versions,
                         None,
                         shopsystem_tested_versions,
                         None,
                         None)
        print("php compat {}".format(self.php_compatibility_versions))
        print("php tested {}".format(self.php_tested_versions))
        print("shopsys tested {}".format(self.shopsystem_tested_versions))

    def update_unit_test_workflow(self):
        """
        Updates unit test workflow with compatible php versions
        """
        workflow_data = FileActionHelper.get_list_data_from_workflow_file(self.extension,
                                                                          Constants.UNIT_TEST_WORKFLOW)
        for line in workflow_data:
            if Constants.PHP_VERSIONS_IN_UNIT_TEST_WORKFLOW + ":" in line:
                new_line = "{}{}\n".format(line[:line.index("[")], str(self.php_compatibility_versions))
                workflow_data[workflow_data.index(line)] = new_line
        with open(FileActionHelper.get_file_path_by_config_key(self.extension, Constants.UNIT_TEST_WORKFLOW), 'w') as f:
            f.writelines(workflow_data)

    def update_ui_test_workflow(self):
        """
        Updates ui test workflow with tested php versions
        """
        workflow_data = FileActionHelper.get_list_data_from_workflow_file(self.extension,
                                                                          Constants.UI_TEST_WORKFLOW)

        php_line = workflow_data[self.get_php_tested_line_index(workflow_data)]
        php_line = php_line.replace(StringActionHelper.find_part_to_replace(php_line), self.php_tested_versions[0])
        workflow_data[self.get_php_tested_line_index(workflow_data)] = php_line
        with open(FileActionHelper.get_file_path_by_config_key(self.extension, Constants.UI_TEST_WORKFLOW), 'w') as f:
            f.writelines(workflow_data)

    def get_php_tested_line_index(self, workflow_data) -> int:
        """
        Returns index of line containing UI test php version
        :return: int
        """
        acceptance_stage_flag = False
        for line in workflow_data:
            if Constants.ACCEPTANCE_TEST_IN_UI_TEST_WORKFLOW in line:
                acceptance_stage_flag = True
            if acceptance_stage_flag and "php" in line:
                return workflow_data.index(line)

    def update_compatible_shop_releases_file(self):
        """
        Updated compatible shop versions file with tested shop system version
        :return:
        """
        with open(FileActionHelper.get_file_path_by_config_key(self.extension,
                                                               Constants.COMPATIBLE_SHOP_RELEASES_FILE),
                  'w') as shop_version_file:
            shop_version_file.writelines(self.shopsystem_tested_versions)
