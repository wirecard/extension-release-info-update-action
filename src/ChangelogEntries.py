from src.FileActionHelper import FileActionHelper
from src.Constants import Constants
from bs4 import BeautifulSoup


class ChangelogEntries:

    def __init__(self, extension, last_released_version):
        self.extension = extension
        self.last_released_version = last_released_version
        self.changelog_entries = []
        self.set_changelog_entries()

    def set_changelog_entries(self):
        last_release_entry = FileActionHelper.get_last_release_markdown_entry_part(self.extension,
                                                                                   self.last_released_version,
                                                                                   'comments')
        comments = []
        for comment in last_release_entry.find_all('li'):
            comments.append(comment.text)
        self.changelog_entries = comments
        print(comments)

    def get_changelog_entries(self):
        return self.changelog_entries
