import configparser


# Utility class to read configurations from a config file.
class ConfigReader:

    # Initialize ConfigReader
    def __init__(self, config_file='config/config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    # Get configuration value as a string
    def get(self, section, key):
        return self.config.get(section, key)

    # Get configuration value as a boolean
    def getboolean(self, section, key):
        return self.config.getboolean(section, key)


config_reader = ConfigReader()
