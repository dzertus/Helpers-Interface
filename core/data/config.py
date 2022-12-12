"""
Config
"""
from pyaml_env import parse_config


class YamlParser:
    """ YamlParser  """
    def __init__(self, fpath):
        """

        :param fpath:
        """
        self.fpath = fpath
        self.data = self.load_yaml()

    def load_yaml(self):
        """

        :return:
        """
        data = parse_config(self.fpath, tag='!HI')
        return data

    def save_yaml(self):
        """

        :return:
        """
        with open(self.fpath, 'w') as f:
            f.close()

