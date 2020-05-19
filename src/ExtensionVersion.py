import git
import re


class ExtensionVersion:

    def __init__(self):
        self.repo = git.Repo(search_parent_directories=True)
        self.release_candidate_version = ''
        self.last_released_version = ''
        self.set_release_candidate_version()
        self.set_last_released_version()

    def set_release_candidate_version(self):
        """
        Sets current release candidate version from branch name
        """
        branch = self.repo.active_branch
        print("=======DEBUG INFORMATION==============\n")
        print("RC version {}\n".format(re.sub('[^\d\.]', '', branch.name)))
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
        print("=======DEBUG INFORMATION==============\n")
        print("Git tags {}\n".format(sorted(self.repo.git.tag(l=True).split('\n'))[-1]))
        tag = sorted(self.repo.git.tag(l=True).split('\n'))[-1]
        # tag = str(self.repo.tags[-1])
        self.last_released_version = tag.replace('v', '')

    def get_last_released_version(self, semver=False) -> str:
        """
            Returns last released version from git tag
            :return: str
            """
        if semver:
            return "v" + self.last_released_version
        return self.last_released_version
