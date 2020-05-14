from src.FileActionHelper import FileActionHelper


class ChangelogEntry:

    def __init__(self, extension, last_released_version):
        self.extension = extension
        self.last_released_version = last_released_version
        self.changelog_entries = []
        self.set_changelog_entries()

    def set_changelog_entries(self):
        """
         Sets comments from latest changelog latest entry
         """
        last_release_entry = FileActionHelper.get_changelog_markdown_entry_part(self.extension,
                                                                                self.last_released_version,
                                                                                'comments')
        comments = []
        for comment in last_release_entry.find_all('li'):
            comments.append(comment.text)
        self.changelog_entries = comments
        print(comments)

    def get_changelog_entries(self):
        """
        Returns list of comments from changelog latest entry
        :return: list
        """
        return self.changelog_entries
