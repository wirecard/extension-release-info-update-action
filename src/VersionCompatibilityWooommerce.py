from src.VersionCompatibility import VersionCompatibility


class VersionCompatibilityWoocommerce(VersionCompatibility):

    def __init__(self, extension):
        super().__init__(extension)
        self.compatible_platform_versions = []
        self.tested_platform_versions = []

        self.compatible_platform_versions()
        self.tested_platform_versions()