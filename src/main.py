from src.PhpVersion import PhpVersion
from src.ExtensionVersion import ExtensionVersion
from src.ShopSystemVersion import ShopSystemVersion
from src.Constants import Constants
from src.ChangelogEntry import ChangelogEntry
from src.ChangelogUpdater import ChangelogFileUpdater
from src.InternalFileUpdater import InternalFileUpdater
import argparse
import os


def add_new_changelog_entry_and_update_internal_files(extension_name):
    """
    Updates CHANGELOG file with the new release candidate entry
    :param extension_name:
    :return:
    """
    php_version = PhpVersion(extension_name)
    extension_version = ExtensionVersion()
    print("extension rc version = {}".format(extension_version.get_release_candidate_version(semver=True)))
    print("extension last version = {}".format(extension_version.get_last_released_version(semver=True)))
    shopsystem_version = ShopSystemVersion(extension_name, extension_version.get_last_released_version(semver=True))

    changelog_updater = ChangelogFileUpdater(extension_name,
                                             extension_version.get_release_candidate_version(semver=True),
                                             extension_version.get_last_released_version(semver=True),
                                             php_version.get_compatible_php_versions_from_config(),
                                             php_version.get_tested_php_versions_from_config(),
                                             shopsystem_version.get_compatible_shopsystem_versions_range(),
                                             shopsystem_version.get_tested_shopsystem_versions_range(),
                                             shopsystem_version.get_compatible_platform_versions_range(),
                                             shopsystem_version.get_tested_platform_versions_range())
    changelog_updater.add_new_release_entry_to_changelog()
    internal_file_updater = InternalFileUpdater(extension_name,
                                                extension_version.get_release_candidate_version(),
                                                extension_version.get_last_released_version(),
                                                php_version.get_compatible_php_versions_from_config(),
                                                php_version.get_tested_php_versions_from_config(),
                                                shopsystem_version.get_compatible_shopsystem_versions_range(),
                                                shopsystem_version.get_tested_shopsystem_versions_range(),
                                                shopsystem_version.get_compatible_platform_versions_range(),
                                                shopsystem_version.get_tested_platform_versions_range())
    internal_file_updater.update_files()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Provide shop extension name as an argument.')
    parser.add_argument('repository', metavar='extension name', type=str,
                        help='shop extension name e.g. woocommerce-ee')
    parser.add_argument('action', metavar='action name', type=str,
                        help='the action to be performed e.g. initial_changelog_and_version_update, '
                             'check_changlog_updated',
                        choices=['initial_changelog_and_version_update', 'check_changlog_updated'])

    args = parser.parse_args()
    try:
        extension_name = Constants.EXTENSION_NAMING_CONVENTION[args.repository]
    except KeyError:
        raise Exception("Unknown extension name {}".format(args.repository))
    action = args.action
    version_extension = ExtensionVersion()
    print("=======DEBUG INFORMATION==============\n")
    print("Current working dir: {} \n".format(os.getcwd()))
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print("File list: {} \n".format(files))

    print("=======================================\n")
    if args.action == "initial_changelog_and_version_update":
        add_new_changelog_entry_and_update_internal_files(extension_name)

#   if action == check_changlog_updated
#       get all versions from changelog
#       get all versions from config
#       check if config file versions are different with versions from config
#           update config files with new versions
#       update all other files with new versions
