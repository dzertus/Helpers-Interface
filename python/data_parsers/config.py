#!/usr/bin/python2

import yaml
from yaml.loader import SafeLoader

import re

ENV_VAR_EXP = re.compile(r'\$\{([^}^{]+)\}')

class YamlParser:
    def __init__(self, fpath=None):
        self.fpath = fpath
        self.data = None

        yaml.add_implicit_resolver('!path', path_matcher)
        yaml.add_constructor('!path', path_constructor)

    def load_yaml(self):
        with open(self.fpath) as f:
            self.data = yaml.load(f, Loader=SafeLoader)
            f.close()

    def save_yaml(self):
        with open(self.fpath, 'w') as f:
            self.latest_data = yaml.dump(self.data, f)
            f.close()

    def path_constructor(self, loader, node):
          '''
          Extract the matched value, expand env variable, and replace the match
          from this thread
          https://stackoverflow.com/questions/52412297/how-to-replace-environment-variable-value-in-yaml-file-to-be-parsed-using-python
          '''
          value = node.value
          match = path_matcher.match(value)
          env_var = match.group()[2:-1]
          return os.environ.get(env_var) + value[match.end():]
