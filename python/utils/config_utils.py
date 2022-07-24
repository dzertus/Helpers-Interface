import yaml
from yaml.loader import SafeLoader

def load_yaml(path):
    with open(path) as f:
        data = yaml.load(f, Loader=SafeLoader)
        f.close()
        return data

def save_yaml(path, data):
    with open(path, 'w') as f:
        data = yaml.dump(data, f)
        f.close()