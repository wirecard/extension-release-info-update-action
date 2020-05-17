class Constants:

   #  File names
   # SHOP_EXTENSION_INTERNAL_FILES_JSON_FILE_PATH = '/usr/bin/shop-extensions-internal-files.json'
    # SHOP_EXTENSION_CONFIG_FILES_JSON_FILE_PATH = '/usr/bin/shop-extensions-internal-files.json'
    SHOP_EXTENSION_INTERNAL_FILES_JSON_FILE_PATH = 'shop-extensions-internal-files.json'
    SHOP_EXTENSION_CONFIG_FILES_JSON_FILE_PATH = 'shop-extensions-config-files.json'

    # File name hints
    UNIT_TEST_WORKFLOW = 'unit_test_workflow'
    UI_TEST_WORKFLOW = 'ui_test_workflow'
    CHANGELOG_FILE = 'changelog_file'
    COMPATIBLE_SHOP_RELEASES_FILE = 'compatible_shop_releases_file'
    README_FILE = "README"

    # special strings
    INTERNAL_CHANGELOG_ENTRY_NAME = '== Changelog =='
    PHP_IN_README_ENTRY_NAME = "php_versions"

    # special strings in CHANGELOG.md file
    COMPATIBILITY_IN_CHANGELOG = "Compatibility"
    TESTED_IN_CHANGELOG = "Tested"
    OVERVIEW_IN_CHANGELOG = "Overview"
    TABLE_TAG_IN_CHANGELOG = 'p'
    RELEASE_HEADER_TAG_IN_CHANGELOG = 'h2'
    COMMENTS_TAG_IN_CHANGELOG = 'ul'
    PHP_IN_CHANGELOG = "PHP"
    TABLE_COLUMN_SPLITTER_IN_CHANGELOG = "|"
    TICK_SIGN_IN_CHANGELOG = "&#9989;"
    TICK_SIGN_IN_CHANGELOG_UNICODE = u"\u2705"
    CROSS_SIGN_IN_CHANGELOG = ":x:"
    ROW_SEPARATOR_IN_CHANGELOG = ":-------:"
    NEW_LINE = '\n'

    # values
    EXTENSION_NAMING_CONVENTION = {
        "paymentSDK-php": "paymentsdk",
        "prestashop-ee": "prestashop",
        "woocommerce-ee": "woocommerce",
        "opencart-ee": "opencart",
        "magento2-ee": "magento2",
        "shopware-ee": "shopware",
        "oxid-ee": "oxid",
        "magento-ee": "magento"
    }
