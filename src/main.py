import argparse
from src.VersionPhp import VersionPhp
from src.VersionExtension import VersionExtension
from src.VersionCompatibility import VersionCompatibility
from src.Constants import Constants
from src.ChangelogEntries import ChangelogEntries

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Provide shop extension name as an argument.')
    parser.add_argument('repository', metavar='extension name', type=str,
                        help='shop extension name e.g. woocommerce-ee')
    parser.add_argument('action', metavar='action name', type=str,
                        help='the action to be performed e.g. update_changelog, check_changlog_updated',
                        choices=['update_changelog', 'check_changlog_updated'])

    args = parser.parse_args()
    extension_name = Constants.EXTENSION_NAMING_CONVENTION[args.repository]
    extension_action = args.action
    version_php = VersionPhp(extension_name)

    print("Php compatible version: {} ".format(version_php.get_compatible_php_versions()))
    print("Php tested version: {} ".format(version_php.get_tested_php_versions()))
    version_extension = VersionExtension()
    print("Release candidate version: {} ".format(version_extension.get_release_candidate_version()))
    print("Release candidate version: {} ".format(version_extension.get_last_released_version()))
    print("Release candidate semver version: {} ".format(version_extension.get_last_released_version()))
    # version_compatibility = VersionCompatibility(extension_name,
    #                                              version_extension.get_last_released_version(True))
    version_compatibility = VersionCompatibility(extension_name,
                                                 'v3.2.1')
    print("Compatible shop system versions: {} ".format(
        version_compatibility.get_compatible_shopsystem_versions_range()))
    print("Compatible platform versions: {} ".format(version_compatibility.get_compatible_platform_versions_range()))
    print("Tested shop system versions: {} ".format(
        version_compatibility.get_tested_shopsystem_versions_range()))
    print("Tested platform versions: {} ".format(version_compatibility.get_tested_platform_versions_range()))

    changelog_entries = ChangelogEntries(extension_name, 'v3.2.1')
    print("Changelog entries: {} ".format(changelog_entries.get_changelog_entries()))
