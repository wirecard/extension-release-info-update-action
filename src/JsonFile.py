import json
from collections import namedtuple
import os


class JsonFile:
    def __init__(self, json_file_name):
        self.json_file_name = json_file_name

    def get_json_file(self) -> dict:
        with open(os.path.abspath(self.json_file_name)) as file_name:
            return json.load(file_name)

    @staticmethod
    def json_decoder(extensions_parameters) -> tuple:
        return namedtuple('X', extensions_parameters.keys())(*extensions_parameters.values())

    def get_json_content(self) -> str:
        json_string = json.dumps(self.get_json_file(), indent=4)
        return json.loads(json_string, object_hook=JsonFile.json_decoder)
