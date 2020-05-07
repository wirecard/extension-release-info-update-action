import git
import re


class VersionExtension:

    def __init__(self):
        self.version = ''

    @staticmethod
    def set_current_release_version(self):
        """
        Sets current release version from branch name
        """
        repo = git.Repo(search_parent_directories=True)
        branch = repo.active_branch
        self.version = re.sub('[^\d\.]', '', branch.name)


    @staticmethod
    def get_current_release_version(self) -> str:
        """
        Returns current release version from branch name
        :return: str
        """
        return self.version
