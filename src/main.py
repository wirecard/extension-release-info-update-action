from src.PhpVersion import PhpVersion
from src.ExtensionVersion import ExtensionVersion
from src.ShopSystemVersion import ShopSystemVersion
from src.Constants import Constants
from src.ChangelogEntry import ChangelogEntry
from src.ChangelogUpdater import ChangelogFileUpdater
from src.InternalFileUpdater import InternalFileUpdater
from src.ConfigFileUpdater import ConfigFileUpdater
from src.FileActionHelper import FileActionHelper
import argparse
import sys
from termcolor import colored, cprint


def add_new_changelog_entry_and_update_internal_files(extension_name):
    """
    Updates CHANGELOG file with the new release candidate entry
    :param extension_name:
    :return:
    """
    php_version = PhpVersion(extension_name)
    extension_version = ExtensionVersion()
    print("{} Release candidate version: {} {}".format(Constants.PRETTY_LOG_ADDITION,
                                                       extension_version.get_release_candidate_version(semver=True),
                                                       Constants.PRETTY_LOG_ADDITION))
    print("{} Last released version: {} {}".format(Constants.PRETTY_LOG_ADDITION,
                                                   extension_version.get_last_released_version(semver=True),
                                                   Constants.PRETTY_LOG_ADDITION))

    shopsystem_version = ShopSystemVersion(extension_name, extension_version.get_last_released_version(semver=True))

    changelog_updater = ChangelogFileUpdater(extension_name,
                                             extension_version.get_release_candidate_version(semver=True),
                                             extension_version.get_last_released_version(semver=True),
                                             php_version.get_compatible_php_versions_from_config(),
                                             php_version.get_tested_php_versions_from_config(),
                                             shopsystem_version.get_compatible_shopsystem_versions_range(),
                                             shopsystem_version.get_tested_shopsystem_versions_range_from_config(),
                                             shopsystem_version.get_compatible_platform_versions_range(),
                                             shopsystem_version.get_tested_platform_versions_range())
    changelog_updater.add_new_release_entry_to_changelog()
    internal_file_updater = InternalFileUpdater(extension_name,
                                                extension_version.get_release_candidate_version(),
                                                extension_version.get_last_released_version(),
                                                php_version.get_compatible_php_versions_from_config(),
                                                php_version.get_tested_php_versions_from_config(),
                                                shopsystem_version.get_compatible_shopsystem_versions_range(),
                                                shopsystem_version.get_tested_shopsystem_versions_range_from_config(),
                                                shopsystem_version.get_compatible_platform_versions_range(),
                                                shopsystem_version.get_tested_platform_versions_range())
    internal_file_updater.update_files()


def update_versions_after_changelog_update(extension_name):
    extension_version = ExtensionVersion()
    php_version = PhpVersion(extension_name, extension_version.get_release_candidate_version(semver=True))
    shopsystem_version = ShopSystemVersion(extension_name,
                                           extension_version.get_release_candidate_version(semver=True))
    changelog_entries = ChangelogEntry(extension_name, extension_version.get_release_candidate_version(semver=True))

    config_file_updater = ConfigFileUpdater(extension_name, php_version.get_compatible_php_versions_from_changelog(),
                                            php_version.get_tested_php_versions_from_changelog(),
                                            shopsystem_version.get_tested_shopsystem_versions_range_from_changelog()
                                            )

    if shopsystem_version.get_tested_shopsystem_versions_range_from_config() != \
            shopsystem_version.get_tested_shopsystem_versions_range_from_changelog():
        print(" {} Shop system tested version has changed in CHANGELOG.md, "
              "updating compatible_shop_releases_file {}".format(Constants.PRETTY_LOG_ADDITION,
                                                                 Constants.PRETTY_LOG_ADDITION))
        config_file_updater.update_compatible_shop_releases_file()
    internal_file_updater = InternalFileUpdater(extension_name,
                                                extension_version.get_release_candidate_version(),
                                                extension_version.get_last_released_version(),
                                                php_version.get_compatible_php_versions_from_changelog(),
                                                php_version.get_tested_php_versions_from_changelog(),
                                                shopsystem_version.get_compatible_shopsystem_versions_range(),
                                                shopsystem_version.get_tested_shopsystem_versions_range_from_changelog(),
                                                shopsystem_version.get_compatible_platform_versions_range(),
                                                shopsystem_version.get_tested_platform_versions_range(),
                                                changelog_entries.get_changelog_entries())
    internal_file_updater.update_files()


def compare_config_file_and_changelog_versions(extension_name):
    extension_version = ExtensionVersion()
    php_version = PhpVersion(extension_name, extension_version.get_release_candidate_version(semver=True))
    exit_flag = False
    if php_version.get_compatible_php_versions_from_config() != \
            php_version.get_compatible_php_versions_from_changelog():
        cprint(colored(" {} "
                      "PHP compatible versions have changed in CHANGELOG.md, "
                      "please update Unit test workflow {} "
                      "{}".format(Constants.PRETTY_LOG_ADDITION,
                                  FileActionHelper.get_file_path_by_config_key(extension_name,
                                                                               Constants.UNIT_TEST_WORKFLOW),
                                  Constants.PRETTY_LOG_ADDITION)), 'red', attrs=['bold'], file=sys.stderr)
        exit_flag = True
    if php_version.get_tested_php_versions_from_config() != php_version.get_tested_php_versions_from_changelog():
        cprint(colored(" {} "
                      "PHP tested versions have changed in CHANGELOG.md, "
                      "please update UI test workflow {} "
                      "{}".format(Constants.PRETTY_LOG_ADDITION,
                                  FileActionHelper.get_file_path_by_config_key(extension_name,
                                                                               Constants.UI_TEST_WORKFLOW),
                                  Constants.PRETTY_LOG_ADDITION)), 'red', attrs=['bold'], file=sys.stderr)
        exit_flag = True
    if exit_flag:
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Provide shop extension name as an argument.')
    parser.add_argument('repository', metavar='extension name', type=str,
                        help='shop extension name e.g. woocommerce-ee')
    parser.add_argument('action', metavar='action name', type=str,
                        help='the action to be performed e.g. initial_changelog_and_version_update, '
                             'update_versions_after_changelog_update, check_config_files_after_changelog_update',
                        choices=['initial_changelog_and_version_update',
                                 'update_versions_after_changelog_update',
                                 'check_config_files_after_changelog_update'])

    args = parser.parse_args()
    try:
        extension_name = Constants.EXTENSION_NAMING_CONVENTION[args.repository]
    except KeyError:
        raise Exception("Unknown extension name {}".format(args.repository))
    action = args.action
    if args.action == "initial_changelog_and_version_update":
        add_new_changelog_entry_and_update_internal_files(extension_name)
    if args.action == "update_versions_after_changelog_update":
        update_versions_after_changelog_update(extension_name)
    if args.action == "check_config_files_after_changelog_update":
        compare_config_file_and_changelog_versions(extension_name)
