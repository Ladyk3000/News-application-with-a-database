from configparser import ConfigParser

class Configuration:
    def __init__(self):
        self.params = None

    def get_config(self, filename, section):
        parser = ConfigParser()
        parser.read(filename)
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
            self.params = db
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
