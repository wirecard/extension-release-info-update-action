import argparse
from src.PhpVersion import PhpVersion
from src.ExtensionVersion import ExtensionVersion
from src.CompatibilityVersion import CompatibilityVersion
from src.Constants import Constants
from src.ChangelogEntry import ChangelogEntry

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

    version_extension = ExtensionVersion()
    print("Release candidate version: {} ".format(version_extension.get_release_candidate_version()))
    print("Release candidate semver version: {} ".format(version_extension.get_release_candidate_version(True)))

    print("Last released version: {} ".format(version_extension.get_last_released_version()))
    print("Last released semver version: {} ".format(version_extension.get_last_released_version(True)))
    # version_compatibility = VersionCompatibility(extension_name,
    #                                              version_extension.get_last_released_version(True))

