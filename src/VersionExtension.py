import git
import re


class VersionExtension:

    def __init__(self):
        self.release_candidate_version = ''
        self.last_released_version = ''
        self.set_release_candidate_version()
        self.set_last_released_version()

    def set_release_candidate_version(self):
        """
        Sets current release candidate version from branch name
        """
        repo = git.Repo(search_parent_directories=True)
        branch = repo.active_branch
        self.release_candidate_version = re.sub('[^\d\.]', '', branch.name)

    def get_release_candidate_version(self, semver=False) -> str:
        """
        Returns current release candidate version from branch name
        :return: str
        """
        if semver:
            return "v" + self.release_candidate_version
        return self.release_candidate_version

    def set_last_released_version(self):
        """
        Sets last release version from git tag
        """
        repo = git.Repo(search_parent_directories=True)
        tag = repo.git.tag(l=True)
        self.last_released_version = tag

    def get_last_released_version(self, semver=False) -> str:
        """
            Returns last released version from git tag
            :return: str
            """
        if semver:
            return "v" + self.last_released_version
        return self.last_released_version
