import os
import glob


class FileFinder:

    @staticmethod
    def get_file_path(file_name):
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
