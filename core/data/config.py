# Template file
"""
Config
"""
from abc import ABC, abstractmethod

#yaml
from pyaml_env import parse_config


class Parser(ABC):
    """ Abstract class """
    def __init__(self,):
        """

        :param fpath:
        """
        self.fpath = None
        self.data = None

    @abstractmethod
    def load(self):
        """

        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def save(self):
        """

        :return:
        """
        raise NotImplementedError

    def add(self):
        """

        :return:
        """
        pass

    def replace(self, input):
        """

        :return:
        """
        pass


class YamlParser(Parser):
    """ YamlParser  """
    def __init__(self, fpath):
        """

        :param fpath:
        """

        self.fpath = fpath
        self.data = self.load()

    def load(self):
        """

        :return:
        """
        data = parse_config(self.fpath, tag='!TAG')
        return data

    def save(self):
        """

        :return:
        """
        with open(self.fpath, 'w') as f:
            f.close()
