import argparse
from src.PhpVersion import PhpVersion
from src.ExtensionVersion import ExtensionVersion
from src.ShopSystemVersion import ShopSystemVersion
from src.Constants import Constants
from src.ChangelogEntry import ChangelogEntry
from src.ChangelogUpdater import ChangelogUpdater


def add_new_changelog_entry(extension_name):
    """
    Updates CHANGELOG file with the new release candidate entry
    :param extension_name:
    :return:
    """
    php_version = PhpVersion(extension_name)
    extension_version = ExtensionVersion()
    shopsystem_version = ShopSystemVersion(extension_name, "v3.2.1")
    # TODO when using real repository uncomment and remove hardcoded versions
    # shopsystem_version = ShopSystemVersion(extension_name, extension_version.get_last_released_version(semver=True))

    changelog_updater = ChangelogUpdater(extension_name,
                                         "v3.2.2",
                                         "v3.2.1",
                                         # extension_version.get_release_candidate_version(semver=True),
                                         # extension_version.get_last_released_version(semver=True),
                                         php_version.get_compatible_php_versions_from_config(),
                                         php_version.get_tested_php_versions_from_config(),
                                         shopsystem_version.get_compatible_shopsystem_versions_range(),
                                         shopsystem_version.get_tested_shopsystem_versions_range(),
                                         shopsystem_version.get_compatible_platform_versions_range(),
                                         shopsystem_version.get_tested_platform_versions_range())
    changelog_updater.add_new_release_entry_to_changelog()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Provide shop extension name as an argument.')
    parser.add_argument('repository', metavar='extension name', type=str,
                        help='shop extension name e.g. woocommerce-ee')
    parser.add_argument('action', metavar='action name', type=str,
                        help='the action to be performed e.g. initial_changelog_update, check_changlog_updated',
                        choices=['initial_changelog_update', 'check_changlog_updated'])

    args = parser.parse_args()
    extension_name = Constants.EXTENSION_NAMING_CONVENTION[args.repository]
    action = args.action

    version_extension = ExtensionVersion()
    add_new_changelog_entry(extension_name)
    # version_compatibility = VersionCompatibility(extension_name,
    #                                              version_extension.get_last_released_version(True))
#   if action == initial_changelog_update
#       get all versions from config
#       update changelog with new entry
#       update all other files with new versions
#   if action == check_changlog_updated
#       get all versions from changelog
#       get all versions from config
#       check if config file versions are different with versions from config
#           update config files with new versions
#       update all other files with new versions
