# Wirecard extension release information update action

This action automates bumping versions during release process of Wirecard extensions.
# What it does
This action can do
- Create new entry in CHANGELOG file and update version information in files listed in ````shop-extensions-internal-files.json````. 
    
    The versions are taken accordingly:
     - extension last released version  - taken from last git tag
     - extension current release version - taken from current branch name
     - php compatible versions - taken from unit test settings (see ````shop-extensions-config-files.json````)
     - php tested versions - taken from UI test settings (see ````shop-extensions-config-files.json````)
     - shop system tested version - taken from UI test settings ((see ````shop-extensions-config-files.json````) -> ````.bin/compatible-shop-releases.txt first```` line)
     - shop system compatible version - taken from previous changelog entry ((see ````shop-extensions-config-files.json````))
     - platform tested version - taken from previous changelog entry (if applicable) (see ````shop-extensions-config-files.json````)
     - platform compatible version - taken from previous changelog entry (if applicable) (see ````shop-extensions-config-files.json````)

- Update version information in files listed in ````shop-extensions-internal-files.json```` and config files (files listed in ````shop-extensions-config-files.json````) according to information from CHANGELOG file
 
    Further information will be completed

## How to setup
1. Setting up creating new entry in CHANGELOG file and updating version information in files listed workflow

    Simply add the action to your workflow
    ````
   - name: Checkout ${{ github.event.repository.name }}
      uses: wirecard/checkout@v2.0.0
      with:
        ref: ${{ github.head_ref }}
   - name: Get tags
      run: git fetch --prune --unshallow  
   - name: Bump all versions
      uses: wirecard/extension-release-info-update-action@master
      with:
        repository: <repository-name>
        action: initial_changelog_and_version_update
    
    ````
    And adapt ````shop-extensions-config-files.json````  and ````shop-extensions-internal-files.json````to your repositories.  

2. Setting up updating version information according to information in CHANGELOG workflow
    Simply add the action to your workflow
    ````
   - name: Checkout ${{ github.event.repository.name }}
      uses: wirecard/checkout@v2.0.0
      with:
        ref: ${{ github.head_ref }}
   - name: Get tags
      run: git fetch --prune --unshallow 
   - name: Bump all versions
      uses: wirecard/extension-release-info-update-action@master
      with:
        repository: <repository-name>
        action: check_changelog_updated
    
    ````
    And adapt ````shop-extensions-config-files.json````  and ````shop-extensions-internal-files.json````to your repositories.  

### Mandatory example shop-extension-internal-files.json
````json
{
  "woocommerce":
    {
      "woocommerce-wirecard-payment-gateway.php":
      {
        "extension_version": "Version:",
        "shopsystem_tested_highest_version": "WC tested up to:",
        "shopsystem_compatible_lowest_version" : "WC requires at least:"
      }
  }
}
````
### Mandatory example shop-extension-config-files.json
````json
{
  "woocommerce":
    {
      "unit_test_workflow": "run_cs_unit_coverage.yml",
      "ui_test_workflow": ".travis.yml",
      "changelog_file": "CHANGELOG.md",
      "compatible_shop_releases_file": "compatible-shop-releases.txt"
    }
}
````

## Short overview of the file structure

### main.py

The ```main.py``` file is the main file called through ```entrypoint.sh``` in the container.  
It calls the required objects in the correct order and executes the necessary methods.