"""
Config
"""
import yaml
from pyaml_env import parse_config


class YamlParser:
    """ YamlParser  """
    def __init__(self, fpath):
        """

        :param fpath:
        """
        self.latest_data = yaml.dump(self.data, fpath)
        self.fpath = fpath
        self.data = self._load_yaml()

    def _load_yaml(self):
        """

        :return:
        """
        data = parse_config(self.fpath, tag='!HI')
        return data

    def _save_yaml(self):
        """

        :return:
        """
        with open(self.fpath, 'w') as f:
            f.close()
