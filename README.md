# Wirecard extension release information updater

This action automates bumping versions during release process of wirecard extensions

extension last released version  - taken from last git tag
extension current release version - taken from current branch name
initial php compatible versions - taken from unit tests
initial php tested versions - taken from UI tests
initial shop system tested version - taken from UI test settings (.bin/compatible-shop-releases.txt first line)
shop system compatible version - taken from previous changelog entry

shop system platforn  tested version - taken from previous changelog entry
shop system platform compatible version - taken from previous changelog entry

