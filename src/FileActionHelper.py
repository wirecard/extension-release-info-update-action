import os
import json
import yaml
import markdown
from src.Definition import Definition


class FileActionHelper:

    @staticmethod
    def get_file_path(file_name) -> str:
        """
        Returns filename path
        :return: string
        """
        file_path = None
        current_path = os.getcwd()
        for root, dirs, files in os.walk(current_path):
            if file_name in files:
                file_path = os.path.abspath(os.path.join(root, file_name))
        return file_path

    @staticmethod
    def get_config_file_name(extension, workflow_type) -> str:
        """
        Returns workflow file name
        :return: string
        """
        with open(Definition.SHOP_EXTENSION_CONFIG_FILES_JSON_FILE_PATH, 'r') as config_files_json:
            json_content = json.loads(config_files_json.read())
            workflow_file = json_content[extension][workflow_type]
        return workflow_file

    @staticmethod
    def get_file_path_by_config_key(extension, key):
        config_file_name = FileActionHelper.get_config_file_name(extension, key)
        config_file_full_path = FileActionHelper.get_file_path(config_file_name)
        return config_file_full_path

    @staticmethod
    def get_data_from_workflow_file(extension, workflow) -> yaml:
        """
        Returns data from workflow file
        :return: yaml object
        """
        yaml_data = None
        workflow_file_full_path = FileActionHelper.get_file_path_by_config_key(extension, workflow)
        with open(workflow_file_full_path, 'r') as workflow_file:
            yaml_data = yaml.load(workflow_file, Loader=yaml.FullLoader)
        return yaml_data

    @staticmethod
    def get_data_from_markdown_file(extension, markdown_file) -> markdown:
        """
        Returns data from file
        :return: markdown object
        """
        markdown_file_full_path = FileActionHelper.get_file_path_by_config_key(extension, markdown_file)
        with open(markdown_file_full_path, 'r') as markdown_file:
            markdown_data = markdown.markdown(markdown_file.read())
        return markdown_data

