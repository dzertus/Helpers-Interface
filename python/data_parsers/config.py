#!/usr/bin/python2
import yaml
from pyaml_env import parse_config


class YamlParser:
    def __init__(self, fpath=None):
        self.fpath = fpath
        self.data = self.load_yaml()

    def load_yaml(self):
        data = parse_config(self.fpath, tag='!HI')
        return data

    def save_yaml(self):
        with open(self.fpath, 'w') as f:
            self.latest_data = yaml.dump(self.data, f)
            f.close()