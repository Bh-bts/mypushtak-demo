import configparser


class ConfigReader:
    def __init__(self, config_file='config/config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get(self, section, key):
        return self.config.get(section, key)

    def getboolean(self, section, key):
        return self.config.getboolean(section, key)


config_reader = ConfigReader()
