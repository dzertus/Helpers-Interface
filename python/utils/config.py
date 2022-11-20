#!/usr/bin/python2

import yaml
from yaml.loader import SafeLoader

import re



ENV_VARIABLE_EXP = re.compile(r'\$\{([^}^{]+)\}')

def load_yaml(path):
    with open(path) as f:
        data = yaml.load(f, Loader=SafeLoader)
        f.close()
        return data

def save_yaml(path, data):
    with open(path, 'w') as f:
        data = yaml.dump(data, f)
        f.close()

def path_constructor(loader, node):
      '''
      Extract the matched value, expand env variable, and replace the match
      from this thread
      https://stackoverflow.com/questions/52412297/how-to-replace-environment-variable-value-in-yaml-file-to-be-parsed-using-python
      '''
      value = node.value
      match = path_matcher.match(value)
      env_var = match.group()[2:-1]
      return os.environ.get(env_var) + value[match.end():]

# yaml.add_implicit_resolver('!path', ENV_VARIABLE_EXP)
# yaml.add_constructor('!path', path_constructor)
#
# print(data['env'])