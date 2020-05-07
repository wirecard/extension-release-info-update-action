# from lastversion import lastversion
from collections import namedtuple
import os
import json
import argparse
import sys
import git
import re
from src.VersionPhp import VersionPhp
from src.Definition import Definition

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Provide shop extension name as an argument.')
    parser.add_argument('repository', metavar='extension name', type=str, help='shop extension name e.g. woocommerce-ee')
    parser.add_argument('action', metavar='action name', type=str,
                        help='the action to be performed e.g. update_changelog, check_changlog_updated',
                        choices=['update_changelog', 'check_changlog_updated'])

    args = parser.parse_args()
    extension_name = args.repository
    extension_action = args.action
    version = VersionPhp(extension_name, Definition.SHOP_EXTENSION_CONFIG_FILES_JSON_FILE_PATH)
    print(version.get_compatible_php_versions())

